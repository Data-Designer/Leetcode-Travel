'''
Description: 按行搜
version: 
Author: Data Designer
Date: 2021-09-14 09:59:29
LastEditors: Data Designer
LastEditTime: 2021-09-14 12:33:47
'''
#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        def binarySearch(nums,target):
            left, right =  0, n
            if target > nums[-1] or target < nums[0]:
                return False
            while left <= right:
                mid = (left + right)//2
                if target < nums[mid]:
                    right = right -1
                elif target > nums[mid]:
                    left = left + 1
                else:
                    return True
        for i in range(m):
            if binarySearch(matrix[i][:],target):
                return True
        return False
            
        
        
# @lc code=end

