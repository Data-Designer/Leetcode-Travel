'''
Description: 
version: 
Author: Data Designer
Date: 2021-05-08 12:50:58
LastEditors: Data Designer
LastEditTime: 2021-05-08 12:59:46
'''
#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
       while (root.val - p.val)*(root.val-q.val) >0:
            if root.val > p.val:
               root = root.left
            else:
               root  = root.right
       return root
# @lc code=end

