'''
Description: 
version: 
Author: Data Designer
Date: 2021-05-12 19:48:28
LastEditors: Data Designer
LastEditTime: 2021-05-12 19:55:12
'''
#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 第一种类型的动态规划
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if i==0 and j==0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
                elif j == 0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]
# @lc code=end

