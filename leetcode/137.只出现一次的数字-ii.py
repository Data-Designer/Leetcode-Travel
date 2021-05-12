'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-29 22:20:00
LastEditors: Data Designer
LastEditTime: 2021-03-29 22:20:47
'''
#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        dic = Counter(nums)
        dic = {value:key for key,value in dic.items()}
        return dic[1]
# @lc code=end

