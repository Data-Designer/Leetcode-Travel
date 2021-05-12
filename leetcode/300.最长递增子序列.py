'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-05 19:34:04
LastEditors: Data Designer
LastEditTime: 2021-04-05 20:20:23
'''
#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [1]*size
        for i in range(size): # 一位一位的遍历
            for j in range(i): # 遍历当前位置前面的所有dp
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
        
# @lc code=end

