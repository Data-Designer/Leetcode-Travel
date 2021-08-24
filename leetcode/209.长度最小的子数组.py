'''
Description: 滑动窗口
version: 
Author: Data Designer
Date: 2021-08-24 10:49:07
LastEditors: Data Designer
LastEditTime: 2021-08-24 11:17:53
'''
#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        min_len = len(nums)
        for i in range(len(nums)):
            while sum(nums[i:i+min_len])>=target:
                min_len -= 1
        return min_len +1


        
        
# @lc code=end

