'''
Description: 
version: 
Author: Data Designer
Date: 2021-05-08 09:10:11
LastEditors: Data Designer
LastEditTime: 2021-05-08 09:33:50
'''
#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
        size = len(nums)
        j = 0 # 始终会遍历数组
        for i in range(size):
            if nums[i] != 0: # 不等于0的数字全会进行一次交换，顺序其实由i
                nums[i],nums[j] = nums[j],nums[i] # 借助快排的思想
                j += 1
        return nums
            
# @lc code=end

