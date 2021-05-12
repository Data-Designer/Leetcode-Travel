'''
Description: 
version: 
Author: Data Designer
Date: 2020-10-23 14:56:00
LastEditors: Data Designer
LastEditTime: 2020-12-09 17:05:27
'''
#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==0:
            return []
        res = []
        intervals.sort(key=lambda x: x[0])
        for i in intervals:
            if len(res)==0 or res[-1][1]< i[0]:
                res.append(i)
            # 否则右边界进行修改
            res[-1][1] = max(res[-1][1],i[1])
        return res 


# @lc code=end

