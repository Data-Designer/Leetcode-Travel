'''
Description: 
version: 
Author: Data Designer
Date: 2020-11-07 16:57:30
LastEditors: Data Designer
LastEditTime: 2020-11-07 17:33:52
'''
#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        cur = ''
        res = []
        def dfs(cur,left,right):
            if left==0 and right==0:
                res.append(cur)
                return
            if right<left: # 要保证右边括号严格大于左边
                return 
            if left>0:
                dfs(cur+'(',left-1,right)
            if right>0:
                dfs(cur+')',left,right-1)
        dfs(cur,n,n)
        return res
# @lc code=end

