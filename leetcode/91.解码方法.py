'''
Description: 动态规划，从后向前考虑，考虑最后一次；创建数组存储前一位的所有解法
version: 
Author: Data Designer
Date: 2021-05-22 17:22:19
LastEditors: Data Designer
LastEditTime: 2021-05-22 17:43:02
'''
#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        dic = {chr(i+65):i+1 for i in range(26)}
        size = len(s)
        dp_array = [1] + [0] * size # 这里存储的是每一位的解
        for i in range(1,size+1):
            if s[i-1] != '0':
                dp_array[i] += dp_array[i-1] # 第一部分，只有1位
            if i>1 and int(s[i-2:i])<=26 and s[i-2]!='0': # i>1 。不然不存在有2位构成该项
                dp_array[i] += dp_array[i-2] # 第二部分，有2位构成的最终解
        return dp_array[size]


# @lc code=end

