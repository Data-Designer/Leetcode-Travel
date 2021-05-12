'''
Description: 
version: 
Author: Data Designer
Date: 2021-05-08 09:05:27
LastEditors: Data Designer
LastEditTime: 2021-05-08 09:06:11
'''
#
# @lc app=leetcode.cn id=292 lang=python3
#
# [292] Nim 游戏
#

# @lc code=start
class Solution:
    def canWinNim(self, n: int) -> bool:
        # 关键在于给对手留下4块石头
        return n%4 != 0

# @lc code=end

