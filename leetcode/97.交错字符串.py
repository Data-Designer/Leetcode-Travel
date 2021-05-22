'''
Description: 填表，动态规划经典，自己造表，第一行第一列为起始
version: 
Author: Data Designer
Date: 2021-05-22 17:45:04
LastEditors: Data Designer
LastEditTime: 2021-05-22 18:25:15
'''
#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        len_s3 = len(s3)
        if len_s3 != len_s1 + len_s2:
            return False # 注意空出一位放边界条件
        matrix = [[False for i in range(len_s2+1)] for i in range(len_s1+1)] # 构造矩阵
        matrix[0][0] = True # 边界条件
        for i in range(1, len_s1+1):
            matrix[i][0] = matrix[i-1][0] and s1[i-1] == s3[i-1] # 对应位置相等，而且前i-1位置也应该相等才满足
        for j in range(1, len_s2+1):
            matrix[0][j] = matrix[0][j-1] and s2[j-1] ==s3[j-1] # 之所以减一因为从1开始
        for i in range(1,len_s1+1):
            for j in range(1,len_s2+1): # 因为从1开始所以都要-1
                matrix[i][j] = (matrix[i-1][j] and s1[i-1] == s3[i+j-1]) or (matrix[i][j-1] and s2[j-1] == s3[i+j-1])
        return matrix[-1][-1]

# @lc code=end

