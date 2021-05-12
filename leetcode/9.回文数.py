'''
Description: 
version: 
Author: Data Designer
Date: 2020-10-26 17:48:11
LastEditors: Data Designer
LastEditTime: 2020-10-26 17:52:51
'''
#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==''.join(list(reversed(str(x))))
# @lc code=end

