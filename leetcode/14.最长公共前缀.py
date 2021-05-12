'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-07 16:03:22
LastEditors: Data Designer
LastEditTime: 2021-03-07 16:16:25
'''
#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 特例判断
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        min_len = 0
        size = len(strs)
        # 可以先进行排序优化,升序排列
        strs = sorted(strs,key=lambda x : len(x))
        # 取决于最小的字符串
        flag = strs[0]
        # 只有所有内容都有相同前部时候才行
        flag_size = len(strs[0])
        for i in range(flag_size):
            for j in range(1,size):
                if strs[j][i] == strs[0][i]:
                    continue
                else:
                    return strs[0][:min_len]
            min_len += 1
        return strs[0][:min_len]
                    
            
# @lc code=end

