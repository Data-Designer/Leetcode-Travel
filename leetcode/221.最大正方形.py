'''
Description: 动态规划，dp[i][j]为右下角，由左，左上，上决定
version: 
Author: Data Designer
Date: 2021-08-30 09:47:55
LastEditors: Data Designer
LastEditTime: 2021-08-30 10:06:34
'''
#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) ==0 or len(matrix[0])==0:
            return 0
        maxSide = 0
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == '0':
                    dp[row][col] = 0
                else:
                    if row ==0 or col == 0:
                        dp[row][col] = 1
                    else:
                        dp[row][col] = min(dp[row-1][col],dp[row][col-1],dp[row-1][col-1])+1
                maxSide =  max(maxSide,dp[row][col])
        return maxSide * maxSide
        
# @lc code=end

