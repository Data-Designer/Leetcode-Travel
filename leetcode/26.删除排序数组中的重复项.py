'''
Description: 
version: 
Author: Data Designer
Date: 2020-12-10 13:21:53
LastEditors: Data Designer
LastEditTime: 2020-12-10 13:34:35
'''
#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i<len(nums):
            if i>0 and nums[i]==nums[i-1]:
                nums.remove(nums[i])
                i = i-1 # 这里的len(nums)很重要
            i = i+1
        return len(nums)

# @lc code=end

