'''
Description: 
version: 
Author: Data Designer
Date: 2021-05-10 13:33:38
LastEditors: Data Designer
LastEditTime: 2021-05-10 13:38:33
'''
#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:] # divmod函数模拟进位
# @lc code=end

