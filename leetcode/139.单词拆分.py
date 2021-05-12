'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-05 20:33:04
LastEditors: Data Designer
LastEditTime: 2021-04-05 21:12:26
'''
#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        size = len(s)
        dp = [False]* (size + 1) # 空出一个起始位
        dp[0] = True # 初始状态
        for i in range(size): # 到i为结尾的数
            for j in range(i+1,size+1): # 注意左闭右开的边界条件
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1] # j记录的其实是后一位
# @lc code=end

