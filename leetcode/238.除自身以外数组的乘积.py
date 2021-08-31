'''
Description: 使用L和R两个链表
version: 
Author: Data Designer
Date: 2021-08-31 09:20:24
LastEditors: Data Designer
LastEditTime: 2021-08-31 09:42:27
'''
#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # from functools import reduce
        # res = []
        # for i in range(len(nums)):
        #     res.append(reduce(lambda x,y: x*y,nums[:i]+nums[i+1:]))
        # return res
        size = len(nums)
        L = [1]*size
        R = [1]*size
        for i in range(1,size):
            L[i] = L[i-1] * nums[i-1]
        for i in range(size-2,-1,-1): # 这里注意size
            R[i] = R[i+1] * nums[i+1]
        for i in range(size):
            nums[i] = L[i] * R[i]
        return nums

        
# @lc code=end

