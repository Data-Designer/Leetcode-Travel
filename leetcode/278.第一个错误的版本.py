'''
Description: 
version: 
Author: Data Designer
Date: 2021-05-05 13:25:53
LastEditors: Data Designer
LastEditTime: 2021-05-05 13:36:44
'''
#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 二分
        left,right = 1,n
        while left < right:
            mid = (left + right)//2
            if isBadVersion(mid):
                right = mid -1
            else:
                left = mid + 1
        return left if isBadVersion(left) else left + 1

        
# @lc code=end

