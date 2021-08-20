'''
Description: 动态规划
version: 
Author: Data Designer
Date: 2021-08-20 09:26:48
LastEditors: Data Designer
LastEditTime: 2021-08-20 09:42:05
'''
#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # min(f[amount-coins[0]]+1,.....)
        dp=  [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if i - coin>=0:
                    dp[i] = min(dp[i-coin]+1,dp[i])
        return dp[-1] if dp[-1] != float('inf') else -1

# @lc code=end

