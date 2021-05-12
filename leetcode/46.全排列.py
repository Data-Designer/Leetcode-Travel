'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-11 17:10:40
LastEditors: Data Designer
LastEditTime: 2021-04-28 21:44:36
'''
#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums,tmp):
            # tmp用于存储
            if not nums:
                res.append(tmp)
                return 
            else:
                for i in range(len(nums)): # 建议画树
                    backtrack(nums[:i]+nums[i+1:],tmp+[nums[i]])
        backtrack(nums,[])
        return res
# @lc code=end

