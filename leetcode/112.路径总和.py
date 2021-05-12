'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-12 22:44:35
LastEditors: Data Designer
LastEditTime: 2021-04-12 23:02:04
'''
#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        # 典型的dfs
        if not root.left and not root.right:
            return root.val == targetSum
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
            

# @lc code=end

