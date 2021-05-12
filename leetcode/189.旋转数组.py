'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-15 22:11:47
LastEditors: Data Designer
LastEditTime: 2021-04-15 23:06:17
'''
#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # size = len(nums)
        # k = k % size
        # for i in range(k):
        #     tmp = nums[-1]
        #     for i in range(size-1,0,-1):
        #         nums[i] = nums[i-1]
        #     nums[0] = tmp
        # size = len(nums)
        # k = k % size
        # reverse = nums[-1:-k-1:-1]
        # flag = k
        # for i in range(size-1,k-1,-1): # 尾插法
        #     nums[i] = nums[flag]
        #     flag = flag - 1
        # print(nums)
        # for i in range(k):
        #     nums[i] = reverse[k-i-1]
        # print(reverse)
        size = len(nums)
        k = k % size
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

            

# @lc code=end

