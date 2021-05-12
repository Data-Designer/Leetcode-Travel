import re
class SolutionInfo:
    ObjVal = 0 # 变量隶属于这个类，是类变量
    X = [[]]
    Y = [[[]]]
    U = []
    P = []
    T = []
    Tt = []
    route_Truck = []
    route_UAV = []
    
    def getSolution(self, data, model):
        solution = SolutionInfo() 
        solution.ObjVal = model.ObjVal
        # X_ij
        solution.X = [([0] * data.nodeNum) for j in range(data.nodeNum)] 
        # Y_ijk
        solution.Y = [[([0] * data.nodeNum) for j in range(data.nodeNum)] for i in range(data.nodeNum)]
        # U_i
        solution.U = [[0] for i in range(data.nodeNum)] 
        # P_ij
        solution.P = [[[0] for j in range(data.nodeNum)] for i in range(data.nodeNum)]
        # T_i, T_i'
        solution.T = [[0] for i in range(data.nodeNum)]
        solution.Tt = [[0] for i in range(data.nodeNum)]
        
        for m in model.getVars():
            str = re.split(r"_", m.VarName)
            if(str[0] == "X" and m.x == 1):
                solution.X[int(str[1])][int(str[2])] = m.x
                print(str, end = "")
                print(" = %d" % m.x)
            elif(str[0] == "Y" and m.x == 1):
                solution.Y[int(str[1])][int(str[2])][int(str[3])] = m.x
            elif(str[0] == "U" and m.x > 0) :
                solution.U[int(str[1])] = m.x
            elif(str[0] == "T" and m.x > 0):
                solution.T[int(str[1])] = m.x 
            elif(str[0] == "Tt" and m.x > 0):
                solution.Tt[int(str[1])] = m.x
            elif(str[0] == "P" and m.x > 0):
                solution.P[int(str[1])][int(str[2])] = m.x  
        
        # get the route of truck and UAV
        j = 0
        for i in range(data.nodeNum):
            i = j  # note that the variable is whether is a local variable or a global variable
            for j in range(data.nodeNum):
                if(solution.X[i][j] == 1):
                    solution.route_Truck.append(i)
                    print(" %d -" % i, end = " ")
                    break
        print(" 0") 
        solution.route_Truck.append(0)

        print("\n\n ------Route of UAV ------- ")
        count = 0
        for i in range(data.nodeNum):
            for j in range(data.nodeNum):
                for k in range(data.nodeNum):
                    if(solution.Y[i][j][k] == 1):
                        count  = count + 1
                        #print("UAV %d : %d - %d - %d" % (count, i, j, k))   
                        temp = [i, j, k]
                        solution.route_UAV.append(temp)
        
        for i in range(len(solution.route_Truck)):
            print(" %d " %  solution.route_Truck[i], end = " ")
        print()
        
        print("\n\n ------Route of UAV ------- ")
        for i in range(len(solution.route_UAV)):
            for j in range(len(solution.route_UAV[0])):
                print("UAV %d : %d - %d - %d" % (i, solution.route_UAV[i][0], solution.route_UAV[i][1], solution.route_UAV[i][2]))    
        
        return solution 
                
       