'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-20 21:23:12
LastEditors: Data Designer
LastEditTime: 2021-04-20 21:53:00
'''
#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return None
        premax = nums[0]
        premin = nums[0]
        res = nums[0]
        for num in nums[1:]:
            curmax = max(premax*num,premin*num,num)
            curmin = min(premin*num,premax*num,num)
            res = max(res,curmax,curmin)
            premax = curmax
            premin = curmin
        return res

# @lc code=end

