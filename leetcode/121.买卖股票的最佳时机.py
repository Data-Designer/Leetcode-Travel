'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-30 22:54:43
LastEditors: Data Designer
LastEditTime: 2021-04-01 22:32:07
'''
#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_ = 0
        # size = len(prices)
        # for i in range(size):
        #     for j in range(i,size):
        #         if prices[j]-prices[i]>max_:
        #             max_ = prices[j]-prices[i]
        # return max_
        size = len(prices)
        i,j = 0,size-1
        low,high =prices[i],prices[j] # 这是最低和最高的
        res = 0
        while i<=j:
            low = min(prices[i],low)
            tmp1 = prices[i]-low if prices[i]-low >0 else 0
            high = max(prices[j],high)
            tmp2 = high- prices[j] if high-prices[j] >0 else 0
            i = i+1
            j = j-1
            res = max(high-low,0,tmp1,tmp2,res) # 要和原来的比！
            
        return res
# @lc code=end

