'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-29 18:52:37
LastEditors: Data Designer
LastEditTime: 2021-04-29 19:23:14
'''
#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.backtrack(root) != -1 # 如果不等于-1
    
    def backtrack(self,root):
        if not root:
            return 0
        left = self.backtrack(root.left)
        if left == -1: # 为什么要判断这个呢
            return -1
        right = self.backtrack(root.right)
        if right == -1:
            return -1
        return max(left,right)+1 if abs(left-right)<2 else -1
        
# @lc code=end

