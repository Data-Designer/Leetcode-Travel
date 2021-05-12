'''
Description: 
version: 
Author: Data Designer
Date: 2021-05-05 13:41:18
LastEditors: Data Designer
LastEditTime: 2021-05-05 14:34:14
'''
#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lis = s.split(" ")
        dic = {}
        dic_y = {} # 反向
        size = len(pattern)
        if size != len(lis):
            return False
        for i in range(size):
            if (pattern[i] in dic.keys() and dic[pattern[i]] != lis[i])or (lis[i] in dic_y.keys() and dic_y[lis[i]]!=pattern[i]):
                    return False
            else:
                dic[pattern[i]] = lis[i]
                dic_y[lis[i]] = pattern[i]
        return True
# @lc code=end

