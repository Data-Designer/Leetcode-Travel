'''
Description: 计算重合面积，左下，小取max；右上，大取min,
version: 
Author: Data Designer
Date: 2021-06-01 15:33:29
LastEditors: Data Designer
LastEditTime: 2021-06-01 16:28:25
'''
#
# @lc app=leetcode.cn id=223 lang=python3
#
# [223] 矩形面积
#

# @lc code=start
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # 毫无关联
        A,B,C,D,E,F,G,H = ax1,ay1,ax2,ay2,bx1,by1,bx2,by2
        if D <= F or E >= C or B >= H or G <= A:
            return (D-B) * (C-A) + (H-F) * (G-E)
        # 有所重叠,最直观理解
        left = max(E, A)
        right = min(C, G)
        up = min(H, D)
        down = max(F, B)
        return (D-B) * (C-A) + (H-F) * (G-E) - (up-down) * (right-left)
        
# @lc code=end

