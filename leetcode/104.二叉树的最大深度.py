'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-28 22:05:48
LastEditors: Data Designer
LastEditTime: 2021-04-28 22:13:44
'''
#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

# @lc code=end

