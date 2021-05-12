'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-11 17:22:37
LastEditors: Data Designer
LastEditTime: 2021-03-12 09:40:25
'''
#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums,tmp):
            if not nums and tmp not in res:
                res.append(tmp)
            else:
                for i in range(len(nums)):
                    backtrack(nums[:i]+nums[i+1:],tmp + [nums[i]])
        backtrack(nums,[])
        return res

        
# @lc code=end

