'''
Description: 排序，大于等于其数量就和其相等
version: 
Author: Data Designer
Date: 2021-05-30 09:59:04
LastEditors: Data Designer
LastEditTime: 2021-05-30 10:28:00
'''
#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort() # [0,1,3,5,6]
        size = len(citations)
        if size==0 or citations[-1] ==0: # 特殊情况处理
            return 0
        for i in range(size):
            if citations[i] >= size-i: # 就是大于等于其citation次数的数量和其都相等
                return size-i  # n-i表示大于等于citation的数量
        
# @lc code=end

