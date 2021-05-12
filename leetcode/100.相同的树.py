'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-28 21:51:08
LastEditors: Data Designer
LastEditTime: 2021-04-28 22:05:02
'''
#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    #     if not p and not q:
    #         return True
    #     if not p or not q:
    #         return False
    #     res_q = []
    #     res_p = []
    #     self.dfs(p,res_p)
    #     self.dfs(q,res_q)
    #     if res_p == res_q:
    #         return True
    #     else:
    #         return False
        
    # def dfs(self,root,res):
    #     if not root:
    #         return 
    #     self.dfs(root.left,res)
    #     res.append(root.val)
    #     self.dfs(root.right,res)
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
            

# @lc code=end

