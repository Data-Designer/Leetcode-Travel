'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-14 11:58:52
LastEditors: Data Designer
LastEditTime: 2021-03-14 12:59:14
'''
#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if len(nums)==1:
        #     return nums[0]
        # res = max(nums) # 这样避免单个值过大
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if sum(nums[i:j+1])>res:
        #             res = sum(nums[i:j+1]) # 这个也是左闭右开
        # return res
        # 动态规划，最大值应该就是加不加后一个
        res = nums[0] # 存储每一个位置数为结尾的最大值
        tmp = 0 # 记录i之前数组的数值
        for i in range(len(nums)):
            tmp = max(nums[i],tmp+nums[i])
            res = max(res,tmp)
        return res
            


# @lc code=end

