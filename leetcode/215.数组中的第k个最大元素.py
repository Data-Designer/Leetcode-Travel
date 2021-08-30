'''
Description: 快排和堆排序在这里要熟悉https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/ji-yu-kuai-pai-de-suo-you-topkwen-ti-jia-ylsd/
version: 
Author: Data Designer
Date: 2021-08-27 09:39:24
LastEditors: Data Designer
LastEditTime: 2021-08-30 09:45:11
'''
#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]
# @lc code=end

