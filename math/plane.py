'''
Description: 
version: 
Author: Data Designer
Date: 2020-10-19 19:05:07
LastEditors: Data Designer
LastEditTime: 2020-11-10 16:42:46
'''

# =========import nec package===========
import re
import math
import numpy
import matplotlib.pyplot as plt
import pandas as pd


from gurobipy import Model,LinExpr,GRB
from datadefine import DataStructure
from datafunction import readData,printData
from solu import SolutionInfo


# =========Read the data===========
data = DataStructure() # Structure
path = r'math/data.txt'

CUSTOMERNUM = 7 # 需要配送客户的数量
readData(data, path, CUSTOMERNUM) # 读句柄
printData(data, CUSTOMERNUM) # 打印建模数据



# =========build the model===========
BIG_M = 10000
# construct the model object
model = Model("FSTSP")

# =========initialize the vara===========
# create variables: Muiti-dimension vector: from inner to outer
# X_ij
X = [[[] for i in range(data.nodeNum)] for j in range(data.nodeNum)] 

# Y_ijk
Y = [[[[] for k in range(data.nodeNum)] for j in range(data.nodeNum)] for i in range(data.nodeNum)]

# U_i
U = [[] for i in range(data.nodeNum)]

# P_ij
P = [[[] for j in range(data.nodeNum)] for i in range(data.nodeNum)]

# T_i, T_i'
T = [[] for i in range(data.nodeNum)]
Tt = [[] for i in range(data.nodeNum)]

# 关键变量的赋值，注意有些约束在这里可以直接define
for i in range(data.nodeNum):
    uname = 'U_' + str(i)
    tname = 'T_' + str(i)
    ttname = 'Tt_' + str(i)
    U[i] = model.addVar(0, data.nodeNum, vtype = GRB.CONTINUOUS, name = uname) # constraint 29
    T[i] = model.addVar(0, BIG_M, vtype = GRB.CONTINUOUS, name = tname) # contraint 30,31
    Tt[i] = model.addVar(0, BIG_M, vtype = GRB.CONTINUOUS, name = ttname)
    for j in range(data.nodeNum):
        xname = 'X_' + str(i) + "_"+ str(j)
        pname = 'P_' + str(i) + "_" + str(j)
        X[i][j] = model.addVar(0, 1, vtype = GRB.BINARY, name = xname) # 这是一个约束对象！！不是简单的列表了
        P[i][j] = model.addVar(0, 1, vtype = GRB.BINARY, name = pname) # contraint 32
        for k in range(data.nodeNum):
            yname = 'Y_' + str(i) + "_" + str(j) + "_" + str(k)
            Y[i][j][k] = model.addVar(0, 1, vtype = GRB.BINARY, name = yname)


# =========Add constraints===========
# create the objective expression(1)
obj = LinExpr(0)
            
# add the objective function into the model        
model.setObjective(T[data.nodeNum - 1], GRB.MINIMIZE)

# constraint (2)
# https://zhuanlan.zhihu.com/p/63337617 约束变量
for j in range(1, data.nodeNum - 1): # 这里需要注意，i的取值范围，否则可能会加入空约束 
    expr = LinExpr(0)
    for i in range(0, data.nodeNum - 1): # i -- N0
        if(i != j):
            expr.addTerms(1, X[i][j]) #这个1是它的系数
            for k in range(1, data.nodeNum): # k -- N+
                if(i != k and j != k):
                    expr.addTerms(1, Y[i][j][k])

    model.addConstr(expr == 1, "c1")
    expr.clear()
        

# constraint (3)
expr = LinExpr(0) # 构造寿命短的对象，临时约束
for j in range(1, data.nodeNum):
    expr.addTerms(1, X[0][j])
model.addConstr(expr == 1, "c2")
expr.clear()

# constraint (4)
expr = LinExpr(0) 
for i in range(data.nodeNum - 1):
    expr.addTerms(1, X[i][data.nodeNum - 1])
model.addConstr(expr == 1.0, "c3")
expr.clear()

# constraint (5)
for i in range(1, data.nodeNum - 1):
    for j in range(1, data.nodeNum):
        if(i != j):
            model.addConstr(U[i] - U[j] + 1 <= BIG_M  - BIG_M * X[i][j], 'c5')
            
   
# constraint (6)
for j in range(1, data.nodeNum - 1):
    expr1 = LinExpr(0)
    expr2 = LinExpr(0)
    for i in range(0, data.nodeNum - 1):
        if(j != i):
            expr1.addTerms(1, X[i][j])
               
    for k in range(1, data.nodeNum):
        if(j != k):
            expr2.addTerms(1, X[j][k])
               
    model.addConstr(expr1 == expr2, "c6")
    expr1.clear()
    expr2.clear()


# constraint (7)
for i in range(data.nodeNum - 1):
    expr = LinExpr(0)
    for j in range(1, data.nodeNum - 1):
        if(i != j ):
            for k in range(1, data.nodeNum):
                if(i != k and j != k):
                    expr.addTerms(1, Y[i][j][k])
    model.addConstr(expr <= 1, 'c7')
    expr.clear()        

# constraint (8)
for k in range(1, data.nodeNum):
    expr = LinExpr(0)
    for i in range(0, data.nodeNum - 1):
        if(i != k ):
            for j in range(1, data.nodeNum - 1):
                if(j != i and j != k):
                    expr.addTerms(1, Y[i][j][k])
    model.addConstr(expr <= 1, 'c8')
    expr.clear()
    

# constraint (9)
for i in range(1, data.nodeNum - 1):
    for j in range(1, data.nodeNum):
        for k in range(1, data.nodeNum):
            if(i != j and i != k and j != k):
                expr1 = LinExpr(0)
                expr2 = LinExpr(0)
                for h in range(data.nodeNum - 1):
                    if(h != i):
                        expr1.addTerms(1, X[h][i])
                for l in range(1, data.nodeNum - 1):
                    if(l != k):
                        expr2.addTerms(1, X[l][k])
                model.addConstr(2 * Y[i][j][k] <= expr1 + expr2, "c9")
                expr1.clear()
                expr2.clear()

# constraint (10)
for j in range(1, data.nodeNum - 1):
    for k in range(1, data.nodeNum):
        if(j != k):
            expr = LinExpr(0)
            for h in range(1, data.nodeNum - 1):
                expr.addTerms(1, X[h][k])
            model.addConstr(Y[0][j][k] <= expr, "c10")
            expr.clear()

# constraint (11)
for i in range(1, data.nodeNum - 1):
    for k in range(1, data.nodeNum):
        if(k != i):
            expr = LinExpr(0)
            for j in range(1, data.nodeNum - 1):
                if(i != j and j != k):
                    expr.addTerms(BIG_M, Y[i][j][k])
            model.addConstr(U[k] - U[i] >= 1 - BIG_M + expr, "c11")
            expr.clear()

# constraint (12)
for i in range(1, data.nodeNum - 1):
    expr = LinExpr(0)
    for j in range(1, data.nodeNum - 1):
        for k in range(1, data.nodeNum):
            if(j != i and i != k and j != k):
                expr.addTerms(BIG_M, Y[i][j][k])
    model.addConstr(Tt[i] >= T[i] - BIG_M + expr, "c12")
    expr.clear()

# constraint (13)
for i in range(1, data.nodeNum - 1):
    expr = LinExpr(0)
    for j in range(1, data.nodeNum - 1):
        for k in range(1, data.nodeNum):
            if(j != i and i != k and j != k):
                expr.addTerms(BIG_M, Y[i][j][k])
    model.addConstr(Tt[i] <= T[i] + BIG_M - expr, "c13")
    expr.clear()

# constraint (14)
for k in range(1, data.nodeNum):
    expr = LinExpr(0)
    for i in range(0, data.nodeNum - 1):
        for j in range(1, data.nodeNum - 1):
            if(j != i and i != k and j != k):
                expr.addTerms(BIG_M, Y[i][j][k])
    model.addConstr(Tt[k] >= T[k] - BIG_M + expr, "c14")
    expr.clear()            

# constraint (15)
for k in range(1, data.nodeNum):
    expr = LinExpr(0)
    for i in range(0, data.nodeNum - 1):
        for j in range(1, data.nodeNum - 1):
            if(j != i and i != k and j != k):
                expr.addTerms(BIG_M, Y[i][j][k])
    model.addConstr(Tt[k] <= T[k] + BIG_M - expr, "c15")
    expr.clear()   

# constraint (16)
for h in range(data.nodeNum - 1):
    for k in range(1, data.nodeNum):
        if(h != k):
            expr1 = LinExpr(0)
            expr2 = LinExpr(0)
            for l in range(1, data.nodeNum - 1):
                for m in range(1, data.nodeNum):
                    if(k != l and k != m and l != m):
                        expr1.addTerms(data.lunchingTime, Y[k][l][m])
            
            for i in range(data.nodeNum - 1):
                for j in range(1, data.nodeNum - 1):
                    if(i != j and i != k and j != k):
                        expr2.addTerms(data.recoverTime, Y[i][j][k])
            model.addConstr(T[k] >= T[h] + data.disMatrix[h][k] + expr1 + expr2 - BIG_M + BIG_M * X[h][k], "c16")
            expr1.clear()
            expr2.clear()

# constraint (17)
for j in range(1, data.nodeNum - 1):
    for i in range(data.nodeNum - 1):
        if(i != j):
            expr = LinExpr(0)
            for k in range(1, data.nodeNum):
                if(i != k and j != k):
                    expr.addTerms(BIG_M, Y[i][j][k])
            model.addConstr(Tt[j] >= Tt[i] + data.disMatrix[i][j] - BIG_M + expr, "c17")
            expr.clear()

# constraint (18)
for j in range(1, data.nodeNum - 1):
    for k in range(1, data.nodeNum):
        if(k != j):
            expr = LinExpr(0)
            for i in range(data.nodeNum - 1):
                if(i != k and i != j):
                    expr.addTerms(BIG_M, Y[i][j][k])
            model.addConstr(Tt[k] >= Tt[j] + data.disMatrix[j][k] + data.recoverTime - BIG_M + expr, "c18")
            expr.clear()

# constraint (19)
for k in range(1, data.nodeNum):
    for j in range(1, data.nodeNum - 1):
        for i in range(data.nodeNum - 1):
            if(i != j and i != k and j != k):
                model.addConstr(Tt[k] - Tt[j] + data.disMatrix[i][j] <= data.range_ + BIG_M - BIG_M * Y[i][j][k], "c19")

# constraint (20)
for i in range(1, data.nodeNum - 1):
    for j in range(1, data.nodeNum - 1):
        if(i != j):
            model.addConstr(U[i] - U[j] >= 1 - BIG_M * P[i][j], "c20")

# constraint (21)
for i in range(1, data.nodeNum - 1):
    for j in range(1, data.nodeNum - 1):
        if(i != j):
            model.addConstr(U[i] - U[j] <= -1 +BIG_M - BIG_M * P[i][j], "c21")

# constraint (22)
for i in range(1, data.nodeNum - 1):
    for j in range(1, data.nodeNum - 1):
        if(i != j):
            model.addConstr(P[i][j] + P[j][i] == 1, "c22")

# constraint (23)
for i in range(data.nodeNum - 1):
    for k in range(1, data.nodeNum):
        for l in range(1, data.nodeNum - 1):
            if(k != i and l != i and l != k):
                expr1 = LinExpr(0)
                expr2 = LinExpr(0)
                for j in range(1, data.nodeNum - 1):
                    if(k != j and i != j):
                        expr1.addTerms(BIG_M, Y[i][j][k])
                for m in range(1, data.nodeNum - 1):
                    for n in range(1, data.nodeNum):
                        if(l != m and l != n and m != n):
                            expr2.addTerms(BIG_M, Y[l][m][n])
                model.addConstr(Tt[l] >= Tt[k] - 3*BIG_M + expr1 + expr2 + BIG_M * P[i][l], "c23")
                expr1.clear()
                expr2.clear()

# constraint (24)
model.addConstr(T[0] == 0, "c24")

# constraint (25)
model.addConstr(Tt[0] == 0, "c25")

# constraint (26)
for j in range(1, data.nodeNum - 1):
    model.addConstr(P[0][j] == 1, "c26")

# constraint (27)
for i in range(data.nodeNum):
    for j in range(data.nodeNum):
        if(i == j):
            model.addConstr(X[i][j] == 0, "c27")
        for k in range(data.nodeNum):
            if(i == j or i == k or k == j):
                model.addConstr(Y[i][j][k] == 0, "c28")
                      

# =========solve the model===========
model.write('./plane.lp') # 方便查看
model.Params.timelimit = 10000 # 最大运行时间
model.optimize() # 求解



# =========print the solution info===========
solution = SolutionInfo()
solution = solution.getSolution(data, model)
print("\n\n\n\n-----optimal value-----")
print("Obj: %g" % solution.ObjVal)
print("\n\n ------Route of truck------")
j = 0
for i in range(data.nodeNum):
    i = j  # note that the variable is whether is a local variable or a global variable
    for j in range(data.nodeNum):
        if(solution.X[i][j] == 1):
            print(" %d -" % i, end = " ")
            break
print(" 0") 
print("\n\n ------Route of UAV ------- ")
count = 0
for i in range(data.nodeNum):
    for j in range(data.nodeNum):
        for k in range(data.nodeNum):
            if(solution.Y[i][j][k] == 1):
                count  = count + 1
                print("UAV %d : %d - %d - %d" % (count, i, j, k))



# =========plot the result===========
# draw the route graph

# draw all the nodes first
fig = plt.figure(0)
plt.xlabel('x')
plt.ylabel('y')
plt.title('All Customers')
plt.scatter(data.cor_X[0], data.cor_Y[0], c='blue', alpha=1, marker=',', linewidths=5, label='depot')
plt.scatter(data.cor_X[1:-1], data.cor_Y[1:-1], c='magenta', alpha=1, marker='o', linewidths=5, label='customer') # c='red'定义为红色，alpha是透明度，marker是画的样式


# draw the route
for i in range(data.nodeNum):
    for j in range(data.nodeNum):
        if(solution.X[i][j] == 1):
            x = [data.cor_X[i], data.cor_X[j]]
            y = [data.cor_Y[i], data.cor_Y[j]]
            plt.plot(x, y, 'b', linewidth = 3)

for i in range(data.nodeNum):
    for j in range(data.nodeNum):
        for k in range(data.nodeNum):
            if(solution.Y[i][j][k] == 1):
                x = [data.cor_X[i], data.cor_X[j], data.cor_X[k]]
                y = [data.cor_Y[i], data.cor_Y[j], data.cor_Y[k]]
                plt.plot(x, y, 'r--', linewidth = 3)

                    
plt.grid(True)
plt.legend(loc='best')
plt.show()          
