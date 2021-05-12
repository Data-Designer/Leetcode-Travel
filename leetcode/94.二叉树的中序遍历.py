'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-10 14:30:23
LastEditors: Data Designer
LastEditTime: 2021-04-10 14:51:14
'''
#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # if not root:
        #     return []
        # return  self.inorderTraversal(root.left) + [root.val] +self.inorderTraversal(root.right)
        white,gray = 0,1
        if not root:
            return []
        res = []
        stack = [(white,root)]
        while stack:
            color,node = stack.pop()
            if not node:
                continue # 这里需要继续
            if color==white:
                stack.append((white,node.right))
                stack.append((gray,node))
                stack.append((white,node.left)) # 因为pop也是从结尾进行pop，所以需要反序
            else:
                res.append(node.val)

        return res
        
        
# @lc code=end

