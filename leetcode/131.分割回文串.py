'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-21 16:22:01
LastEditors: Data Designer
LastEditTime: 2021-04-21 16:26:48
'''
#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ishwc = lambda x: x==x[::-1]
        res = []
        self.backtrack(s,res,[])
        return res
    
    def backtrack(self,s,res,path):
        if not s:
            res.append(path)
            return
        for i in range(1,len(s)+1):
            if self.ishwc(s[:i]):
                self.backtrack(s[i:], res, path+[s[:i]]) # 创建的是path新数组
# @lc code=end

