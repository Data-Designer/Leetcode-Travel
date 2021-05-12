'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-21 20:59:17
LastEditors: Data Designer
LastEditTime: 2021-04-21 21:00:30
'''
#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)
        return nums[size//2]
# @lc code=end

