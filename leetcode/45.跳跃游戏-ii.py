'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-05 08:28:19
LastEditors: Data Designer
LastEditTime: 2021-04-05 09:22:29
'''
#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        step = 0
        max_arrive = 0
        end = 0 # 每一次的边界
        for i in range(n-1): # 不需要访问倒数第1个元素
            max_arrive = max(max_arrive,nums[i]+i)
            if i == end :
                # 如果到达边界处,更新边界，而且无论在哪走都要走一步
                end = max_arrive
                step = step + 1
        return step
                
# @lc code=end

