'''
Description: dfs。从边界开始搜索
version: 
Author: Data Designer
Date: 2021-06-04 10:00:47
LastEditors: Data Designer
LastEditTime: 2021-06-04 10:16:30
'''
#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
from typing import Collection


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        row = len(board)
        col = len(board[0])
        def dfs(i,j):
            if i<0 or j<0 or i>=row or j >=col or board[i][j]!='O':
                return
            board[i][j] = 'B' # 标记搜索过
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        for i in range(row):
            dfs(i,0)
            dfs(i,col-1)
        for j in range(col):
            dfs(0,j)
            dfs(row-1,j) # 边界条件
        for i in range(row):
            for j in range(col):
                if board[i][j] =="B":
                    board[i][j] ="O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        
# @lc code=end

