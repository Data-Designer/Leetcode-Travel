'''
Description: 
version: 
Author: Data Designer
Date: 2020-11-03 23:18:16
LastEditors: Data Designer
LastEditTime: 2020-11-03 23:45:31
'''
#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for i in nums:
        #     if i == target:
        #         return nums.index(i)
        # return -1
        if not nums:
            return -1
        left,right = 0,len(nums)-1
        while left<=right:
        # 数组从任意一个地方劈开都至少有一半是有序的
        # 我们只判断其是否在有序列表中
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            # 如果左半段有序
            if nums[mid]>=nums[left]:
                if nums[left]<=target<=nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid]<=target<=nums[right]:
                    left = mid+1
                else:
                    right = mid-1 # 丢弃这一半
        # 搜索完毕还未返回
        return -1

        
# @lc code=end

