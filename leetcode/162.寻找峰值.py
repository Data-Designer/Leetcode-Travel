'''
Descript: 只要相邻的大，一定可以找到峰值
version: 
Author: Data Designer
Date: 2021-08-12 19:28:25
LastEditors: Data Designer
LastEditTime: 2021-08-12 19:59:31
'''
#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        l,r = 0,N-1
        while l<r:
            mid = l+(r-l)//2
            if nums[mid]>nums[mid+1]:
                r = mid
            else:
                l = mid+1
        return l



            
# @lc code=end

