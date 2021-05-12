'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-05 07:55:37
LastEditors: Data Designer
LastEditTime: 2021-04-05 08:01:17
'''
#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip().split(" ")
        if s[-1] != "":
            return len(s[-1])
        else:
            return 0
# @lc code=end

