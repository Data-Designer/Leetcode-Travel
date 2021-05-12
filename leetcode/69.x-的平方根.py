'''
Description: 
version: 
Author: Data Designer
Date: 2020-12-08 23:39:24
LastEditors: Data Designer
LastEditTime: 2020-12-09 00:06:33
'''
#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # if x==0:
        #     return 0
        # if x==1:
        #     return 1
        # for i in range(x+1):
        #     if i*i<=x:
        #         continue
        #     else:
        #         return i-1
        if x ==1:
            return 1
        left,right = 0,x
        mid = 0
        while left<right:
            mid = (left+right)//2+1 # 2
            if mid*mid == x:
                return mid 
            elif mid*mid>x:
                right = mid-1 # right=3
            else:
                left = mid  # 3
        return right
            

# @lc code=end

