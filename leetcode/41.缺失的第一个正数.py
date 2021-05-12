'''
Description: 
version: 
Author: Data Designer
Date: 2020-12-16 08:25:37
LastEditors: Data Designer
LastEditTime: 2020-12-16 09:14:29
'''
#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 1
        # nums.sort()
        # max_ = nums[-1]
        # if max_ <=0:
        #     return 1
        # else:
        #     for i in range(1,max_):
        #         if i not in nums:
        #             return i
        # return max_+1
        #使用hash表思想
        if not nums:
            return 1
        size = len(nums)
        for i in range(size):
            # i位置存储的是数字i+1
            while 1<=nums[i]<=size and nums[i] != nums[nums[i]-1]:
                self._swap(nums,i,nums[i]-1)
        for i in range(size):
            if i+1 != nums[i]:
                return i+1
        return size+1 # 都找不到返回N+1

    def _swap(self,nums,index1,index2):
        nums[index1],nums[index2] = nums[index2],nums[index1]

        
        
# @lc code=end

