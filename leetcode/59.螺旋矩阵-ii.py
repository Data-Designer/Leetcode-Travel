'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-12 10:24:20
LastEditors: Data Designer
LastEditTime: 2021-03-14 10:48:28
'''
#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        l,r,t,b = 0,n-1,0,n-1
        tar = n*n
        mat = 1 #待填入的数
        res = [[0 for i in range(n)] for i in range(n)] # 待填入的矩阵
        while  mat<=tar:
            for i in range(l,r+1):
                res[t][i] = mat
                mat = mat+1
            t = t + 1
            for i in range(t,b+1):
                res[i][r] = mat
                mat = mat+1
            r = r-1
            for i in range(r,l-1,-1):
                res[b][i] = mat
                mat = mat+1
            b = b-1
            for i in range(b,t-1,-1): # 这里必须指定-1
                res[i][l] = mat
                mat = mat+1
            l = l+1
        return res
# @lc code=end

