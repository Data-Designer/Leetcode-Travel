'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-21 21:44:21
LastEditors: Data Designer
LastEditTime: 2021-03-21 21:53:40
'''
#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        res = [[1],[1,1]]
        for i in range(2,rowIndex+1):
            tmp = []
            for j in range(i+1):
                if j==0 or j== i:
                    tmp.append(1)
                else:
                    tmp.append(res[i-1][j-1]+res[i-1][j])
            res.append(tmp)
        return res[-1] # 从0开始
# @lc code=end

