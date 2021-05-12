'''
Description: 
version: 
Author: Data Designer
Date: 2021-05-12 19:56:15
LastEditors: Data Designer
LastEditTime: 2021-05-12 20:26:16
'''
#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 把第一行，第一列当作标志位
        row_flag = False
        col_flag = False # 防止第一行第一列无效
        row = len(matrix)
        col = len(matrix[0]) # 这种表征
        for j in range(col):
            if matrix[0][j] == 0:
                row_flag = True
                break
        for i in range(row):
            if matrix[i][0] == 0:
                col_flag = True
                break
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        # 检查,第二遍扫描
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][0]==0 or matrix[0][j] ==0:
                    matrix[i][j] = 0
        # 防止标志位本身也是
        if row_flag:
            for j in range(col):
                matrix[0][j] = 0
        if col_flag:
            for i in range(row):
                matrix[i][0] = 0

# @lc code=end

