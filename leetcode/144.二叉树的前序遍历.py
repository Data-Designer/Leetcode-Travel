'''
Description: 
version: 
Author: Data Designer
Date: 2021-05-27 09:20:14
LastEditors: Data Designer
LastEditTime: 2021-05-27 09:29:27
'''
#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.preorder(res,root)
        return res

    def preorder(self,res,root):
        if not root:
            return []
        res.append(root.val)
        self.preorder(res,root.left)
        self.preorder(res,root.right)

# @lc code=end

