'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-16 20:36:24
LastEditors: Data Designer
LastEditTime: 2021-03-16 20:45:41
'''
#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        if n==0:
            return False
        # 直接chu除干净就行
        while n%2 ==0:
            n = n//2
        while n%5 ==0:
            n = n//5
        while n%3==0:
            n=n//3
        if n!=1:
            return False
        else:
            return True
                
# @lc code=end

