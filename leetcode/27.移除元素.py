'''
Description: 
version: 
Author: Data Designer
Date: 2020-12-10 13:34:41
LastEditors: Data Designer
LastEditTime: 2020-12-10 13:39:08
'''
#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        nums.sort()
        while i<len(nums):
            if nums[i]==val:
                nums.remove(val)
                i = i-1
            i = i+1
        return len(nums)

# @lc code=end

