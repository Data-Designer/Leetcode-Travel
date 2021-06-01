'''
Description: dp[i][j] = dp[i-1][j-1],dp[i-1][j] + triangle[i][j]
version: 
Author: Data Designer
Date: 2021-06-01 20:43:49
LastEditors: Data Designer
LastEditTime: 2021-06-01 21:16:18
'''
#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0]*n for i in range(n)]
        dp[0][0] = triangle[0][0] # 初始条件
        for i in range(1,n):
            dp[i][0] = dp[i-1][0]+ triangle[i][0] # 当前位置
            for j in range(1,i): # 第i行有i个数
                dp[i][j] = min(dp[i-1][j],dp[i-1][j-1])+triangle[i][j] # 转移方程
            dp[i][i] = dp[i-1][i-1] + triangle[i][i] # 边界条件
        return min(dp[n-1])
                
        
# @lc code=end

