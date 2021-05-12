'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-29 19:29:40
LastEditors: Data Designer
LastEditTime: 2021-04-29 19:38:14
'''
#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left,root.right = root.right,root.left
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root
# @lc code=end

