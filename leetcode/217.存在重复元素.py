'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-26 12:30:37
LastEditors: Data Designer
LastEditTime: 2021-04-26 12:31:46
'''
#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        dic = Counter(nums)
        for i in dic.items():
            if i[1]>1:
                return True
        return False
# @lc code=end

