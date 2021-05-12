'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-01 22:36:26
LastEditors: Data Designer
LastEditTime: 2021-04-01 22:48:11
'''
#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = 0
        for i in range(1,len(prices)):
            if prices[i]-prices[i-1] > 0:
                profits = profits + (prices[i]-prices[i-1]) # 隔天交易于连续相邻交易
        return profits
# @lc code=end

