'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-16 18:33:13
LastEditors: Data Designer
LastEditTime: 2021-03-16 19:02:46
'''
#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l,r,t,b = 0,len(matrix[0])-1,0,len(matrix)-1
        tar = (r+1)*(b+1)
        res = []
        flag = 1
        while  flag<=tar:
            for i in range(l,r+1):
                res.append(matrix[t][i])
                flag = flag+1
            t = t + 1
            for i in range(t,b+1):
                res.append(matrix[i][r])
                flag = flag+1
            r = r - 1
            for i in range(r , l-1, -1):
                res.append(matrix[b][i])
                flag = flag+1
            b = b - 1
            for i in range(b, t-1 , -1):
                res.append(matrix[i][l])
                flag = flag+1
            l = l + 1
        return res[:tar] # 有点迷，里面为啥会有多的数


            
# @lc code=end

