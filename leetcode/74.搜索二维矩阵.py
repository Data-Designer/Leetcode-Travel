'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-16 22:31:56
LastEditors: Data Designer
LastEditTime: 2021-03-16 23:00:34
'''
#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target >matrix[-1][-1]:
            return False
        # ends = matrix[:][-1] # 不能这样按列索引
        # print(ends)
        
        left, right = 0,len(matrix)-1
        while left <= right:
            mid = left + (right-left)//2
            if matrix[mid][-1]==target:
                return True
            elif matrix[mid][-1] < target:
                left = mid+1
            else:
                right = mid-1
        if left > len(matrix)-1:
            # 有时候没找到会越界
            left = left - 1
        if target not in matrix[left][:]:
            return False
        return True
        
            
# @lc code=end

