'''
Description: affect别的格子，简化规则，10位上2-3个活细胞，原活则活，10位上3个活细胞，原死则活
version: 
Author: Data Designer
Date: 2021-05-30 21:39:12
LastEditors: Data Designer
LastEditTime: 2021-05-30 21:55:06
'''
#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        def affect(x,y):
            for i in [x-1,x,x+1]:
                for j in [y-1,y,y+1]: # 注意边界条件
                    if i<0 or i>=m or j<0 or j>=n or (i==x and j==y):
                        continue
                    board[i][j]+=10 # 活格子影响周围
        for i in range(m):
            for j in range(n):
                if board[i][j] %10 ==1: # 只有活格子才能影响周围
                    affect(i,j)
                    
        def calculate(i,j): # 简化条件
            value = board[i][j]
            if value // 10 ==3:
                board[i][j] = 1
            elif value // 10 == 2 and value %10 ==1:
                board[i][j] =1
            else:
                board[i][j] =0
                
        for i in range(m):
            for j in range(n):
                calculate(i,j)
        
# @lc code=end

