'''
Description: 
version: 
Author: Data Designer
Date: 2021-05-06 21:46:49
LastEditors: Data Designer
LastEditTime: 2021-05-06 21:57:11
'''
#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        size_1 = len(s)
        size_2 = len(t)
        if size_1 != size_2:
            return False
        dic_1 = {}
        dic_2 = {}
        for i in range(size_1):
            if (s[i] in dic_1.keys() and t[i] != dic_1[s[i]]) or (t[i] in dic_2.keys() and s[i]!=dic_2[t[i]]):
                return False
            else:
                dic_1[s[i]] = t[i]
                dic_2[t[i]] = s[i] # 双向检查
        return True

        
# @lc code=end

