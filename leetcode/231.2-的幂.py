'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-05 20:22:52
LastEditors: Data Designer
LastEditTime: 2021-04-05 20:28:05
'''
#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n== 0:
            return False
        while n%2 ==0 :
            n = n//2
        if n==1:
            return True
        else:
            return False

# @lc code=end

