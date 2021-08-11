'''
Description: 动态规划
version: 
Author: Data Designer
Date: 2021-08-10 20:46:05
LastEditors: Data Designer
LastEditTime: 2021-08-10 20:55:43
'''
#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp =  [0]*(N+1) # 多一位
        dp[0],dp[1] = 0,nums[0] # 特殊情况
        for i in range(2,N+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1]) # 这里的dp[i]其实是i-1个房子
        return dp[-1]

# @lc code=end

