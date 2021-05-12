'''
Description: 
version: 
Author: Data Designer
Date: 2021-05-10 22:45:50
LastEditors: Data Designer
LastEditTime: 2021-05-10 23:17:34
'''
#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
       res = 0
       for i in range(32):
           # 32个位
            res = res << 1 | n & 1 # n取最低位，然后换到res那边
            n >>= 1 # https://zhuanlan.zhihu.com/p/28018082
       return res
# @lc code=end

