'''
Description: dfs。陆地沉没或者陆地变高
version: 
Author: Data Designer
Date: 2021-06-03 09:37:27
LastEditors: Data Designer
LastEditTime: 2021-06-03 10:02:57
'''
#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        res=0
        for i in range(r):
            for j in range(c):
                if grid[i][j] =='1': # 注意是字符串
                    self.dfs(grid,r,c,i,j)
                    res += 1
        return res

    def dfs(self,grid,r,c,i,j):
        if not 0<=i<r or not 0<=j<c:
            return
        if grid[i][j] != '1': # base case，防止出错
            return 
        grid[i][j] = 2 # 陆地上升
        self.dfs(grid,r,c,i-1,j)
        self.dfs(grid,r,c,i+1,j)
        self.dfs(grid,r,c,i,j-1)
        self.dfs(grid,r,c,i,j+1)



# @lc code=end

