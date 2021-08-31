'''
Description: 使用树的遍历
version: 
Author: Data Designer
Date: 2021-08-31 09:43:26
LastEditors: Data Designer
LastEditTime: 2021-08-31 09:49:00
'''
#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        res = 0
        while queue:
            root = queue.pop()
            res += 1
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        return res
# @lc code=end

