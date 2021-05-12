'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-16 20:46:08
LastEditors: Data Designer
LastEditTime: 2021-03-16 21:20:47
'''
#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 就是2，3，5的组合
        # 三指针法
        res = [1]
        id2 = 0
        id3 = 0
        id5 = 0
        for i in range(n-1):
            res.append(min(res[id2]*2,res[id3]*3,res[id5]*5))
            if res[-1] == res[id2]*2:
                id2 = id2+1
            if res[-1] == res[id3]*3:
                id3 = id3+1
            if res[-1] == res[id5]*5: # 肯定是由前面的某个数*2或者*3得到的
                id5 = id5+1
        return res[-1]
# @lc code=end

