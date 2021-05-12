'''
Description: 
version: 
Author: Data Designer
Date: 2020-11-03 23:46:12
LastEditors: Data Designer
LastEditTime: 2020-11-04 09:00:00
'''
#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        if size ==0:
            return [-1,-1]
        first_place = self.__findfirstplace(nums,target,size)
        if first_place == -1:
            # 最后left和right可是要重合的
            return [-1,-1]
        last_place = self.__findlastplace(nums,target,size)
        return [first_place,last_place]


    def __findfirstplace(self,nums,target,size):
        left,right = 0,size-1
        while left<right:
            mid = (left+right)//2
            if nums[mid]<target:
                left = mid+1
            elif nums[mid]==target:
                right = mid
            else:
                right =mid-1
        if nums[left]==target:
            return left
        else:
            return -1
    
    def __findlastplace(self,nums,target,size):
        left,right =0,size-1
        while left<right:
            mid = (left+right)//2+1 # 如果不加1就会在elif中陷入死循环
            if nums[mid]<target:
                left = mid+1
            elif nums[mid]==target:
                left = mid
            else:
                right = mid-1
        # 能运行这个函数说明肯定有值
        # 反正重合，right和left一样
        return right

# @lc code=end

