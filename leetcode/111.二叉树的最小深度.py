'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-28 22:14:57
LastEditors: Data Designer
LastEditTime: 2021-04-29 09:37:06
'''
#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not root.left and not root.right:
            return 1
        elif not root.left or not root.right:
            return left + 1 if root.left else right + 1
        else:
            return min(left,right)+1
# @lc code=end

