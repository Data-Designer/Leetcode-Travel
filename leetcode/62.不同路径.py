'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-14 10:49:14
LastEditors: Data Designer
LastEditTime: 2021-03-14 11:10:37
'''
#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 使用递归的方法
        res = [[0 for i in range(n)] for i in range(m)] # 行列
        print(res)
        for i in range(m): # 因为只能往下和右,所以这一列出发起始点都是1
            res[i][0] = 1
        for i in range(n):
            res[0][i] = 1 # 防止数组越界
        for i in range(1,m):
            for j in range(1,n):
                res[i][j] = res[i-1][j] + res[i][j-1] # 每个格子等于两个格子和
        return res[-1][-1]
# @lc code=end

