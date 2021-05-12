'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-14 13:14:41
LastEditors: Data Designer
LastEditTime: 2021-04-21 20:58:46
'''
#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p_num1 = m-1
        p_num2 = n-1
        tail = m+n-1
        while p_num1 >= 0 or p_num2 >= 0:
            if p_num1 == -1:
                nums1[tail] = nums2[p_num2]
                p_num2 = p_num2 - 1
            elif p_num2 == -1:
                nums1[tail] = nums1[p_num1]
                p_num1 = p_num1 - 1
            elif nums1[p_num1] >= nums2[p_num2]:
                nums1[tail] = nums1[p_num1]
                p_num1 = p_num1 -1
            else:
                nums1[tail] = nums2[p_num2]
                p_num2 = p_num2 - 1
            tail = tail - 1
        return nums1



       


# @lc code=end

