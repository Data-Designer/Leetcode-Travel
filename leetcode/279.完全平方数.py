'''
Description: dp = min(dp[i],dp[n-i*i]),每一个dp上都存储对应的次数。从后往前思考
version: 
Author: Data Designer
Date: 2021-05-31 09:37:19
LastEditors: Data Designer
LastEditTime: 2021-05-31 10:31:32
'''
#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
import math
from math import floor

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]*(n+1) # dp-0肯定为0
        for i in range(1,n+1): # 注意起始点和终止点
            dp[i] =  i # 最差

            for j in range(1,floor(math.sqrt(i))+1):
                dp[i] = min(dp[i],dp[i-j*j]+1) # 加一次跳跃
        return dp[n]

# @lc code=end

