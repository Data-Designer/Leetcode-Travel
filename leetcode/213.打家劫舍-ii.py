'''
Description:转化为两个标准单排问题
version: 
Author: Data Designer
Date: 2021-08-11 09:17:02
LastEditors: Data Designer
LastEditTime: 2021-08-11 09:36:25
'''
#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        def tworob(nums):
            N = len(nums)
            dp = [0] * (N+1)
            dp[0],dp[1] = 0,nums[0]
            for i in range(2,N+1):
                dp[i] = max(dp[i-1],dp[i-2]+nums[i-1]) # 最后一家不能偷
            return dp[-1]
        return max(tworob(nums[:-1]),tworob(nums[1:])) if len(nums)!=1 else nums[0] # 这个判断条件非常重要
# @lc code=end

