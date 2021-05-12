'''
Description: 
version: 
Author: Data Designer
Date: 2020-10-26 16:05:55
LastEditors: Data Designer
LastEditTime: 2020-10-26 16:14:19
'''
#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        # 溢出的状况不会解
        if str(x)[0] not in ['0','1','2','3','4','5','6','7','8','9']:
            x = str(x)[1:]
            sign = '-'
        else:
            x = str(x)
            sign = '+'
        res = int(sign + ''.join(list(reversed(x))))
        if res<-pow(2,31) or res> pow(2,31)-1:
            return 0
        else:
            return res
# @lc code=end

