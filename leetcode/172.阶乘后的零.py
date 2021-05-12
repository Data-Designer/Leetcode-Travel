'''
Description: 
version: 
Author: Data Designer
Date: 2021-05-10 13:46:49
LastEditors: Data Designer
LastEditTime: 2021-05-10 13:50:46
'''
#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        # 只看5的次数就可以
        for i in range(1,n+1):
            while i%5 ==0: # 10 由2，5组成
                count += 1
                i = i//5
        return count
# @lc code=end

