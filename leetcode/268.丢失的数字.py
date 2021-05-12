'''
Description: 
version: 
Author: Data Designer
Date: 2021-05-05 12:32:36
LastEditors: Data Designer
LastEditTime: 2021-05-05 12:36:01
'''
#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        dic = {}
        for index,value in enumerate(nums):
            dic[value] = index
        for i in range(n):
            if i not in dic.keys():
                return i
        return n # 从0开始的
# @lc code=end

