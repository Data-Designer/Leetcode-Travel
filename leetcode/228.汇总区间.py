'''
Description: 
version: 
Author: Data Designer
Date: 2021-05-05 12:50:26
LastEditors: Data Designer
LastEditTime: 2021-05-05 13:21:09
'''
#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        # 两个指针
        size = len(nums)
        if size == 1:
            return [str(nums[0])]
        slow,fast = 0,0
        while fast<= size-1:
            while fast <=size-1 and nums[fast]-nums[slow] == fast -slow: # 边界条件
                fast = fast + 1
            if fast - slow ==1:
                res.append(str(nums[slow]))
            else:
                res.append(str(nums[slow])+'->'+str(nums[fast-1]))
            slow = fast
        return res

# @lc code=end

