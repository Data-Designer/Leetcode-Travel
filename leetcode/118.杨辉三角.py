'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-21 21:31:16
LastEditors: Data Designer
LastEditTime: 2021-03-21 21:43:20
'''
#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        res = [[1],[1,1]]
        for i in range(2,numRows):
            tmp = []
            for j in range(i+1):
                if j==0 or j== i:
                    tmp.append(1)
                else:
                    tmp.append(res[i-1][j-1]+res[i-1][j])
            res.append(tmp)
        return res
            
# @lc code=end

