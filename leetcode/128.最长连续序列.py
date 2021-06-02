'''
Description: hash table，cur和longer比较
version: 
Author: Data Designer
Date: 2021-05-30 19:24:44
LastEditors: Data Designer
LastEditTime: 2021-06-02 11:42:16
'''
#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest_seq = 0
        nums_set = set(nums)
        for i in nums_set:
            if i-1 not in nums_set:
                cur_num = i
                cur_seq = 0
                while cur_num in nums_set:
                    cur_num = cur_num+1
                    cur_seq +=1
                longest_seq = max(longest_seq,cur_seq)
            else:
                continue
        return longest_seq

        
# @lc code=end

