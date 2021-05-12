'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-14 11:11:08
LastEditors: Data Designer
LastEditTime: 2021-03-14 11:58:01
'''
#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid) # row
        n = len(obstacleGrid[0]) # column
        dp = [[0 for i in range(n)] for j in range(m)]
        # 特例
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        for i in range(1,m):
            # dp[i][0] = 1 万一障碍物在这一行就不行了
            if obstacleGrid[i][0]!=1:
                dp[i][0] = dp[i-1][0]
        for i in range(1,n):
            if obstacleGrid[0][i] !=1: 
                dp[0][i] = dp[0][i-1]
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] ==1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
# @lc code=end

