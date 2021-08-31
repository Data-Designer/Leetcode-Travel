'''
Description: 二叉搜索树的中序遍历是顺序数组
version: 
Author: Data Designer
Date: 2021-08-31 09:54:37
LastEditors: Data Designer
LastEditTime: 2021-08-31 09:57:32
'''
#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []
        def midSearch(root):
            if not root:
                return
            midSearch(root.left)
            res.append(root.val)
            midSearch(root.right)
        midSearch(root)
        return res[k-1]
# @lc code=end

