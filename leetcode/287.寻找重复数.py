'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-14 13:08:53
LastEditors: Data Designer
LastEditTime: 2021-03-14 13:13:45
'''
#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i]==nums[i+1]:
        #         return nums[i]
        # 下面使用hash table
        from collections import defaultdict
        dic = defaultdict()
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                return nums[i]
                
# @lc code=end

