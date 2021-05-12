'''
Description: 
version: 
Author: Data Designer
Date: 2021-05-08 09:37:18
LastEditors: Data Designer
LastEditTime: 2021-05-08 09:44:36
'''
#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_s = {}
        hash_t = {}
        for i in s:
            hash_s[i] = hash_s.get(i,1) + 1
        for i in t:
            hash_t[i] = hash_t.get(i,1) + 1
        if hash_s == hash_t:
            return True
        else:
            return False
# @lc code=end

