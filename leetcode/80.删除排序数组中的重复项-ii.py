'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-21 20:29:23
LastEditors: Data Designer
LastEditTime: 2021-03-21 21:30:47
'''
#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除排序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return 1
        slow,count = 0,1
        for fast in range(1,size):
            if nums[fast]==nums[fast-1]:
                count = count + 1
            else:
                count = 1
            if count <= 2:
                slow = slow + 1
                nums[slow] = nums[fast] # 向前填充
        return slow+1 # 因为返回的是len，所以要加一
        
# @lc code=end

