'''
Description: 
version: 
Author: Data Designer
Date: 2020-12-08 23:08:44
LastEditors: Data Designer
LastEditTime: 2020-12-08 23:37:21
'''
#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickpow(N):
            # 分治思想
            if N==0:
                return 1
            y = quickpow(N//2)
            return y*y if N%2==0 else y*y*x
        return quickpow(n) if n>0 else 1/quickpow(-n)
        
        
# @lc code=end

