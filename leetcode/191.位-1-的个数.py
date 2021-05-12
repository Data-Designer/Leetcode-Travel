'''
Description: 
version: 
Author: Data Designer
Date: 2021-05-10 22:43:37
LastEditors: Data Designer
LastEditTime: 2021-05-10 23:18:57
'''
#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
       res = 0
       for i in range(32):
           flag= 0
           flag = n & 1 # 末尾1位
           if flag == 1:
               res = res + 1
           n >>= 1
       return res

# @lc code=end

