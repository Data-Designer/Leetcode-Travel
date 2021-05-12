'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-29 20:09:42
LastEditors: Data Designer
LastEditTime: 2021-04-29 20:35:59
'''
#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        # num = str(num)
        # while len(num)>=2:
        #     tmp = 0
        #     for i in range(len(num)):
        #         tmp += int(num[i])
        #     num = str(tmp)
        # return int(num)
        if num == 0:
            return 0
        return ((num-1) % 9) + 1
# @lc code=end

