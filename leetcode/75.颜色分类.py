'''
Description: 
version: 
Author: Data Designer
Date: 2021-05-13 09:47:16
LastEditors: Data Designer
LastEditTime: 2021-05-13 10:16:48
'''
#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left,right = 0,len(nums)-1
        cur = 0
        while cur <= right:
            if nums[cur]==0:
                nums[cur],nums[left] = nums[left] ,nums[cur]
                left += 1
                cur +=1
            elif nums[cur]==2:
                nums[cur],nums[right] = nums[right],nums[cur]
                # 此时交换后cur位置有可能是0，不能直接cur增加
                right -=1
            else:
                cur +=1

# @lc code=end

