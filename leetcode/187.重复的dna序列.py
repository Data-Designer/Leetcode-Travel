'''
Description: 
version: 
Author: Data Designer
Date: 2021-08-10 21:05:32
LastEditors: Data Designer
LastEditTime: 2021-08-10 21:18:13
'''
#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        res = set()
        win = 10
        N = len(s)
        for i in range(N-win+1):
            tmp = s[i:i+win]
            if tmp in seen:
                res.add(tmp[:])
            seen.add(tmp)
        return list(res)
            

# @lc code=end

