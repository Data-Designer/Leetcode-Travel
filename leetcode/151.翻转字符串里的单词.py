'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-20 20:59:19
LastEditors: Data Designer
LastEditTime: 2021-04-20 21:10:48
'''
#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        # 使用栈
        s = s.strip().split(" ")
        s.reverse()
        print(s)
        res = ''
        for i in range(len(s)):
            if s[i] !="":
                res = res + " " + s[i]
        res = res.strip()
        return res

# @lc code=end

