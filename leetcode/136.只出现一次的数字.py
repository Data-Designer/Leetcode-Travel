'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-29 22:13:26
LastEditors: Data Designer
LastEditTime: 2021-03-29 22:19:21
'''
#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        dic = dict(Counter(nums))
        dic = {value:key for key,value in dic.items()}
        return dic[1]
# @lc code=end

