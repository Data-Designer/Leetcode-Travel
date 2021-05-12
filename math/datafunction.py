import math
import re
#=========读取数据===========
def readData(data,path,customerNum):
    data.customerNum = customerNum
    data.nodeNum = customerNum + 2 # 从0开始的！仓库和仓库
    f = open(path, 'r')
    lines = f.readlines()
    count = 0
    # read the info
    for line in lines:
        count = count + 1
        if(count == 2):
            line = line[:-1]
            str = re.split(r" +", line)
            data.range = float(str[0])
        elif(count == 5):
            line = line[:-1]
            str = re.split(r" +", line)
            data.lunchingTime = float(str[0])
            data.recoverTime = float(str[1])
        elif(count >= 9 and count <= 9 + customerNum): # (count >= 9 and count <= 9 + customerNum)
            line = line[:-1]
            str = re.split(r" +", line)
            data.cor_X.append(float(str[2]))
            data.cor_Y.append(float(str[3]))
            data.demand.append(float(str[4]))
            data.readyTime.append(float(str[5]))
            data.dueTime.append(float(str[6]))
            data.serviceTime.append(float(str[7]))

    data.cor_X.append(data.cor_X[0])
    data.cor_Y.append(data.cor_Y[0])
    data.demand.append(data.demand[0])
    data.readyTime.append(data.readyTime[0])
    data.dueTime.append(data.dueTime[0])
    data.serviceTime.append(data.serviceTime[0])
    
            
    # compute the distance matrix
    data.disMatrix = [([0] * data.nodeNum) for p in range(data.nodeNum)] # 初始化距离矩阵的维度,防止浅拷贝
    for i in range(0, data.nodeNum):
        for j in range(0, data.nodeNum):
            temp = (data.cor_X[i] - data.cor_X[j])**2 + (data.cor_Y[i] - data.cor_Y[j])**2
            data.disMatrix[i][j] = math.sqrt(temp)
            temp = 0
    
    return data

#=========打印数据===========
def printData(data, customerNum):
    print("下面打印数据\n")
    print("UAV range = %4d" % data.range)
    print("UAV lunching time = %4d" % data.lunchingTime)
    print("UAV recover time = %4d" % data.recoverTime)
    for i in range(len(data.demand)):
        print('{0}\t{1}\t{2}\t{3}'.format(data.demand[i], data.readyTime[i],data.dueTime[i],  data.serviceTime[i]))
    
    print("-------距离矩阵-------\n")
    for i in range(data.nodeNum):
        for j in range(data.nodeNum):
            #print("%d   %d" % (i, j))
            print("%6.2f" % (data.disMatrix[i][j]), end = " ")
        print()