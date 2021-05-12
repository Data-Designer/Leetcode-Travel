'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-05 09:38:50
LastEditors: Data Designer
LastEditTime: 2021-04-05 09:59:49
'''
#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        cur = n # 起始点
        for i in range(100): # 单纯for
            next = 0
            size = len(str(cur))
            for i in range(size):
                next = next + pow(int(str(cur)[i]),2)
                if cur ==1:
                    return True
            cur = next # 赋值给下一个
        return False
# @lc code=end

