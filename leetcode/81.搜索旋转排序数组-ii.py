'''
Description: 二分法
version: 
Author: Data Designer
Date: 2021-05-19 20:06:27
LastEditors: Data Designer
LastEditTime: 2021-05-19 20:40:59
'''
#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        l,r = 0,len(nums)-1
        while l<=r:
            # 二分法
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            if nums[l] == nums[r]:
                l +=1
                continue
            if nums[l]<= nums[mid]:
                # 左边有序
                if nums[l] <= target <nums[mid]:
                    r = mid -1
                else:
                    l = mid +1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid +1
                else:
                    r = mid -1
        return False

# @lc code=end

