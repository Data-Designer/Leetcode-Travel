'''
Description: 具体思路是保证一个最长区间，其中的每一个数都大于区间长度
version: 
Author: Data Designer
Date: 2021-05-30 10:33:55
LastEditors: Data Designer
LastEditTime: 2021-05-30 10:43:46
'''
#
# @lc app=leetcode.cn id=275 lang=python3
#
# [275] H 指数 II
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        size = len(citations)
        if size ==0 or citations[-1]==0:
            return 0
        left,right = 0,size-1
        while left < right:
            mid = left + (right-left)//2
            if citations[mid] >= size-mid: # 因为要保证区间外的每一个数都小于n-i
                right = mid
            else:
                left = mid +1
        return size-left
# @lc code=end

