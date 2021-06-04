'''
Description: 深度优先遍历
version: 
Author: Data Designer
Date: 2021-06-04 09:13:47
LastEditors: Data Designer
LastEditTime: 2021-06-04 09:41:01
'''
#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root,pre_total):
            if not root:
                return 0
            total = pre_total * 10 + root.val
            if not root.left and not root.right: # 明确终止条件为叶子节点
                return total
            else:
                return dfs(root.left,total) + dfs(root.right,total) # 无需存储中间过程
        return dfs(root,0)
# @lc code=end

