'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-29 21:35:14
LastEditors: Data Designer
LastEditTime: 2021-05-12 19:42:50
'''
#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2): # row,col转到col,n-row-1,从后向前写
            for j in range((n+1)//2): # 奇数多转1列
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]

        

# @lc code=end

