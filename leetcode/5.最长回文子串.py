'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-06 16:59:23
LastEditors: Data Designer
LastEditTime: 2021-03-06 20:06:33
'''
#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
    #     # 特判
    #     if len(s)<2:
    #         return s
    #     size = len(s)
    #     max_len = 1
    #     res = s[0]

    #     for i in range(0,size-1):
    #         for j in range(i+1,size):
    #             if j-i+1 > max_len and self.valid(s, i, j):
    #                 max_len = j-i+1
    #                 res = s[i:j+1]
    #     return res



    # def valid(self,s,i,j):
    #     '''验证子串为回文串'''
    #     left = i
    #     right = j
    #     while left <right:
    #         # 子串的子串也必须是回文串
    #         if s[left] != s[right]:
    #             return False
    #         left = left +1
    #         right = right -1
    #     return True
        size = len(s)
        if size < 2:
            return s
        dp = [[False for i in range(size)] for j in range(size)] # 构造动态规划表
        for i in range(size):
            dp[i][i] = True # 初始化,只有一个子串
        
        max_len = 1 # 初始状态是1
        start = 0
        # 下面应该考虑左下角
        for j in range(1,size):
            for i in range(0,j): # i是小的
                if s[i]==s[j]:
                    if j-i<3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1] # 取决于子串
                else:
                    dp[i][j] = False
                if dp[i][j] == True:
                    cur_len = j-i+1
                    if cur_len >max_len:
                        max_len = cur_len
                        start = i

        return s[start:start+max_len]
        
        

# @lc code=end

