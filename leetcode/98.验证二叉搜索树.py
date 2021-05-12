#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = self.dfs_bst(root)
        return res

    def dfs_bst(self,root,lower=float('-inf'),upper = float('inf')):
        if not root:
            return True
        val = root.val
        if val<=lower or val>=upper:
            return False
        if not self.dfs_bst(root.right,val,upper):
            return False
        if not self.dfs_bst(root.left,lower,val): # 如果其子树不满足，直接返回False
            return False
        return True
        
        

# @lc code=end

