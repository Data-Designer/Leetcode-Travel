'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-21 15:39:51
LastEditors: Data Designer
LastEditTime: 2021-04-21 15:50:58
'''
#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 快慢指针,正则
        s = s.lower()
        import re 
        pattern = re.compile(r'[a-z0-9]+')
        res = re.findall(pattern, s)
        s = "".join(res)
        if s[::-1]==s:
            return True
        else:
            return False
# @lc code=end

