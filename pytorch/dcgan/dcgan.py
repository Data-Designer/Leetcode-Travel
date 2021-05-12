import argparse
import os
import random
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.optim as optim
import torch.utils.data
import torchvision.datasets as dset
import torchvision.transforms as transforms
import torchvision.utils as vutils

# 添加参数
parser = argparse.ArgumentParser()
parser.add_argument('--dataset', required=True, help='cifar10 | lsun | mnist |imagenet | folder | lfw | fake')
parser.add_argument('--dataroot', required=False, help='path to dataset')
parser.add_argument('--workers', type=int, help='number of data loading workers', default=2)
parser.add_argument('--batchSize', type=int, default=64, help='input batch size')
parser.add_argument('--imageSize', type=int, default=64, help='the height / width of the input image to network')
parser.add_argument('--nz', type=int, default=100, help='size of the latent z vector')
parser.add_argument('--ngf', type=int, default=64)
parser.add_argument('--ndf', type=int, default=64)
parser.add_argument('--niter', type=int, default=25, help='number of epochs to train for')
parser.add_argument('--lr', type=float, default=0.0002, help='learning rate, default=0.0002')
parser.add_argument('--beta1', type=float, default=0.5, help='beta1 for adam. default=0.5')
parser.add_argument('--cuda', action='store_true', help='enables cuda')
parser.add_argument('--dry-run', action='store_true', help='check a single training cycle works')
parser.add_argument('--ngpu', type=int, default=1, help='number of GPUs to use')
parser.add_argument('--netG', default='', help="path to netG (to continue training)")
parser.add_argument('--netD', default='', help="path to netD (to continue training)")
parser.add_argument('--outf', default='.', help='folder to output images and model checkpoints')
parser.add_argument('--manualSeed', type=int, help='manual seed')
parser.add_argument('--classes', default='bedroom', help='comma separated list of classes for the lsun data set')

opt = parser.parse_args()
print(opt)
# mk output dir
try:
    os.mkdir(opt.outf)
except OSError:
    pass

if opt.manualSeed is None:
    opt.manualSeed = random.randint(1,10000)
print("Random Seed: ",opt.manualSeed)
random.seed(opt.manualSeed)
torch.manual_seed(opt.manualSeed) # seed for device for the same num

cudnn.benchmark = True # 为当前input寻找最优算法，increase the effciency(same input dim)

if torch.cuda.is_available() and not opt.cuda:
    print('Waning: U have a cuda,so u should run the cuda')

if opt.dataroot is None and str(opt.dataset).lower !='fake':
    raise ValueError(" `dataroot` paramater is required for dataset \"%s\"" % opt.dataset)

if opt.dataset in ['imagenet','folder','lfw']:
    # fold dataset
    # https://blog.csdn.net/weixin_40123108/article/details/85099449查看ImageFolder的用法
    dataset = dset.ImageFolder(root = opt.dataroot,transform=transforms.Compose([
        transforms.Resize(opt.imageSize),
        transforms.CenterCrop(opt.imageSize),
        transforms.ToTensor(),
        transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5)),
    ]))
    nc = 3 # channel

elif opt.dataset = 'lsun':
    classes = [c+'_train' for c in opt.classes.split(',')]
    dataset= dset.LSUN(root=opt.dataroot,classes=classes,transforms=transforms.Compose([
        transforms.Resize(opt.imageSize),
        transforms.CenterCrop(opt.imageSize),
        transforms.ToTensor(),
        transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5)),
    ]))
    nc = 3
# dataset folder not exist
elif opt.dataset == 'cifar10':
    dataset = dset.CIFAR10(root=opt.dataroot, download=True,
                           transform=transforms.Compose([
                               transforms.Resize(opt.imageSize),
                               transforms.ToTensor(),
                               transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
                           ]))
    nc=3

elif opt.dataset == 'mnist': # define
        dataset = dset.MNIST(root=opt.dataroot, download=True,
                           transform=transforms.Compose([
                               transforms.Resize(opt.imageSize),
                               transforms.ToTensor(),
                               transforms.Normalize((0.5,), (0.5,)),
                           ]))
        nc=1

elif opt.dataset == 'fake':
    dataset = dset.FakeData(image_size=(3, opt.imageSize, opt.imageSize),
                            transform=transforms.ToTensor())

assert dataset
dataloader =  torch.utils.data.DataLoader(dataset,batch_size=opt.batchSize,
            shuffle=True,num_workers=int(opt.workers)) # download
# dataloader:(step,(x,y)) 每个step里面有batch_size个数据

device = torch.device("cuda:0" if opt.cuda else "cpu")
ngpu = int(opt.gpu)
ngf = int(opt.ngf)
nz = int(opt.nz)
ndf = int(opt.ndf)


# weights initial 

def weights_init(m):
    classname = m.__class__.__name__
    if classname.find('Conv') !=1:
        torch.nn.init.normal_(m.weight,0.0,0.02) # m is g and D
    elif classname.find("BatchNorm") !=1:
        torch.nn.init.normal_(m.weight,1.0,0.02)
        torch.nn.init.zeros_(m.bias) # 这个参数？？

class Generator(nn.Module):
    """
    生成
    """
    def __init__(self,ngpu):
        super(Generator,self).__init__()
        self.ngpu = ngpu
        self.main =nn.Sequential([
            # z（input,output,k-size,strid,padding）
            nn.ConvTranspose2d(nz,ngf*8,4,1,0,bias=False), # 反卷积
            nn.BatchNorm2d(ngf*8),
            nn.Relu(True),
            # state size
            nn.ConvTranspose2d(ngf*8,ngf*4,4,2,1,bias=False)
            nn.BatchNorm2d(ngf*4),
            nn.Relu(True),
            #state
            nn.ConvTranspose2d(ngf*4,ngf*2,4,2,1,bias=False)
            nn.BatchNorm2d(ngf*2),
            nn.Relu(True),
            # state
            nn.ConvTranspose2d(ngf*2,ngf,4,2,1,bias=False),
            nn.BatchNorm2d(ngf),
            nn.Relu(True),
            #state
            nn.ConvTranspose2d(ngf,nc,4,2,1,bias=False)
            nn.Tanh() # 最后一层使用Tanh进行激活,生成的是图片才对。
        ])
    def forward(self,input):
        if input.is_cuda and self.ngpu>1:
            output = nn.parallel(self.main,input,range(self.ngpu)) # model,input,gpu
        else:
            output = self.main(input)
        return output

netG = Generator(ngpu).to(device) # net also need to device
netG.apply(weights_init) # init
if opt.netG != '':
    netG.load_state_dict(torch.load(opt.netG)) # if weights exits,directly load
print(netG)

class Discrimitor(nn.Module):
    """
    Discrimitor
    """
    def __init__(self,ngpu):
        super(Discrimitor,self).__init__()
        self.ngpu = ngpu
        self.main = nn.Sequential(
            # input is (nc) x 64 x 64
            nn.Conv2d(nc, ndf, 4, 2, 1, bias=False),
            nn.LeakyReLU(0.2, inplace=True),
            # state size. (ndf) x 32 x 32
            nn.Conv2d(ndf, ndf * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ndf * 2),
            nn.LeakyReLU(0.2, inplace=True),
            # state size. (ndf*2) x 16 x 16
            nn.Conv2d(ndf * 2, ndf * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ndf * 4),
            nn.LeakyReLU(0.2, inplace=True),
            # state size. (ndf*4) x 8 x 8
            nn.Conv2d(ndf * 4, ndf * 8, 4, 2, 1, bias=False),
            nn.BatchNorm2d(ndf * 8),
            nn.LeakyReLU(0.2, inplace=True),
            # state size. (ndf*8) x 4 x 4
            nn.Conv2d(ndf * 8, 1, 4, 1, 0, bias=False),
            nn.Sigmoid() # binary classifier
        )
    def forward(self,input):
        if input.is_cuda and self.ngpu>1:
            output = nn.parallel.data_parallel(self.main,input,range(self.ngpu))
        else:
            output = self.main(output)
        return output.view(-1,1).squeeze(1) # https://blog.csdn.net/york1996/article/details/81949843

netD = Discrimitor(ngpu).to(device)
netD.apply(weights_init)
if opt.netD != '':
    netD.load_state_dict(torch.load(opt.netD))
print(netD)

# loss and optim
criterion = nn.BCELoss()
fixed_noise = torch.randn(opt.batchSize,nz,1,1,device=device) # invoid the mem
real_label = 1
fake_label = 0

optimizerD = optim.Adam(netD.parameters(),lr = opt.lr,betas=(opt.beta1,0.999))
optimizerG = optim.Adam(netG.parameters(),lr = opt.lr,betas=(opt.beta1,0.999))

if opt.dry_run:
    opt.niter = 1
    
for epoch in range(opt.niter):
    for i ,data in enumerate(dataloader,0):
        ### Update D network : maxmize log(D(x)) +log(1-D(x))
        netD.zero_grad() # grad->0而不是intial=0，每个batch都需要做，不然grad就会累加
        real_cpu = data[0].to(device)
        batch_size = real_cpu.size(0)
        #https://blog.csdn.net/claroja/article/details/108316652
        label = torch.full((batch_size,),real_label,dtype=real_cpu.dtype,device=device)
        output = netD(real_cpu)
        errD_real = criterion(output,label)
        errD_real.backward()
        D_x = output.mean().item()

        # train with fake
        # https://blog.csdn.net/qq_31267769/article/details/107882119
        noise = torch.randn(batch_size,nz,1,1,device=device) # 4 dim
        fake = netG(noise)
        label.fill_(fake_label) # http://www.mamicode.com/info-detail-2217311.html 填充替换，这样可以少些变量
        output = netD(fake.detach) # https://blog.csdn.net/qq_39709535/article/details/80804003 截断梯度流，防止更新G参数
        errD_fake = criterion(output,label)
        errD_fake.backward()
        D_G_z1 = output.mean().item()
        errD = errD_real+errD_fake
        optimizerD.step() # 更新参数

        # Update G network:maxmize log(D(G(z)))
        netG.zero_grad()
        label.fill_(real_label)
        output = netD(fake)
        errG = criterion(output,label) # fake labels are real for G，需要让G生成的图片越真越好
        D_G_z2 = output.mean().item()
        optimizerG.step()
        print('[%d/%d][%d/%d] Loss_D: %.4f Loss_G: %.4f D(x): %.4f D(G(z)): %.4f / %.4f'
              % (epoch, opt.niter, i, len(dataloader),
                 errD.item(), errG.item(), D_x, D_G_z1, D_G_z2))

        if i%100==0:
            vutils.save_image(real_cpu,'%s/real_samples.png'%opt.outf,normalize=True) # 真实批次的image
            fake = netG(fixed_noise) # 生成fake的image
            vutils.save_image(fake.detach(),
                    '%s/fake_samples_epoch_%03d.png' % (opt.outf, epoch),
                    normalize=True)
        if opt.dry_run: # ？？？不理解
            break
    # do checkpoints
    torch.save(netG.state_dict,'%s/netG_epoch_%d.pth'%(opt.outf,epoch))
    torch.save(netD.state_dict,'%s/netD_epoch_%d.pth'%(opt.outf,epoch))




