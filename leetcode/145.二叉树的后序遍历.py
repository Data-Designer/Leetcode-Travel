'''
Description: 后序
version: 
Author: Data Designer
Date: 2021-08-25 13:50:11
LastEditors: Data Designer
LastEditTime: 2021-08-25 13:56:47
'''
#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def poster(root):
            if not root:
                return 
            poster(root.left)
            poster(root.right)
            res.append(root.val)
        res = []
        poster(root)
        return res
        
            
        
        
# @lc code=end

