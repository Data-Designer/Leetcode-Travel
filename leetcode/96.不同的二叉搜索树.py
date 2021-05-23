'''
Description: 卡特兰数字，G(n) = G(0)*G(n-1) +......
version: 
Author: Data Designer
Date: 2021-05-23 12:04:18
LastEditors: Data Designer
LastEditTime: 2021-05-23 12:22:00
'''
#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1,1] + [0]*(n-1) # 多留一位,0是空二叉树
        for i in range(2,n+1): # 每次都以i结尾
            for j in range(1,i+1):
                dp[i] += dp[j-1]*dp[i-j] # 注意这里是求sum和
        return dp[n]

# @lc code=end

