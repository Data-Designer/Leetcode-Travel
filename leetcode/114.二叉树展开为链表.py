'''
Description: 可以先序遍历，但是Moris算法（右边移到左最右节点，右边移到左节点，直至右节点为空）
version: 
Author: Data Designer
Date: 2021-05-25 09:43:14
LastEditors: Data Designer
LastEditTime: 2021-05-25 10:04:57
'''
#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if not root.left:
                root = root.right
            else:
                left = root.left
                while left.right:
                    # 当有右节点的时候
                    left = left.right
                left.right = root.right # 右子树移到左子树
                root.right = root.left # 左子树移到右子树
                root.left = None
                root = root.right # 接下去的右节点
        return root

        
# @lc code=end

