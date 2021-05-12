#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        # 左子树左和右子树右对称
        return self.bfs(root.left,root.right)
        '''一个新的想法是前序遍历等于后序遍历'''

    def bfs(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.bfs(left.left,right.right) and self.bfs(left.right,right.left)
# @lc code=end

