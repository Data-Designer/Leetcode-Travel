'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-05 08:10:42
LastEditors: Data Designer
LastEditTime: 2021-04-05 08:25:50
'''
#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_arrive = 0
        for i in range(n):
            if i <= max_arrive:
                max_arrive = max(max_arrive,nums[i]+i) # 位置+自身跳跃
            if max_arrive>=n-1:
                return True
        return False
# @lc code=end

