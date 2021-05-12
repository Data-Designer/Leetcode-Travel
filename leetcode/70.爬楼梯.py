'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-08 23:44:32
LastEditors: Data Designer
LastEditTime: 2021-04-09 00:15:20
'''
#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        # return self.climbStairs(n-1)+self.climbStairs(n-2)
        first, second = 1, 2
        for i in range(2, n+1):
            first, second = second, first+second # 这里的first还没有赋值
            # temp = first+second
            # first = second
            # second = temp
        return a

            
# @lc code=end

