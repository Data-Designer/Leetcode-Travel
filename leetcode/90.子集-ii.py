'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-20 18:00:20
LastEditors: Data Designer
LastEditTime: 2021-03-20 21:52:32
'''
#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort() # 只要去重就一定排序
        check = [0 for i in range(len(nums))] # 判断上一个重复数有没有被用过
        self.backtrack([],0, nums, check)
        return self.res

    def backtrack(self,tmp,index,nums,check):
        self.res.append(tmp) # 从0开始都是有效解
        for i in range(index,len(nums)):
            if i>0 and nums[i] == nums[i-1] and check[i-1]==0:
                continue
            check[i] = 1 # 之前的没用过
            self.backtrack(tmp + [nums[i]],i+1,nums, check) # 下一层
            check[i] = 0 # 用过了

# @lc code=end

