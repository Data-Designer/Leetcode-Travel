'''
Description: 中序【【左】根【右】】，后序【【左】【右】根】
version: 
Author: Data Designer
Date: 2021-05-24 08:54:39
LastEditors: Data Designer
LastEditTime: 2021-05-24 09:26:43
'''
#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        hash_dic = {i:index for index,i in enumerate(inorder)}
        n = len(inorder)
        return self.treeBuild(postorder,inorder,hash_dic,0,n-1,0,n-1)
    
    def treeBuild(self,postorder,inorder,hash_dic,inorder_left,inorder_right,postorder_left,postorder_right):
        # if inorder_left > inorder_right:
        #     return None
        # if inorder_left == inorder_right: 
        #     return TreeNode(inorder[inorder_left]) # 为啥要加这个限制
        if postorder_left > postorder_right:
            return None
        root = TreeNode(postorder[postorder_right])
        inorder_index = hash_dic[postorder[postorder_right]] # 1
        left_size = inorder_index - inorder_left # 左子树长度
        root.left = self.treeBuild(postorder,inorder,hash_dic,inorder_left,inorder_index-1,postorder_left,postorder_left+left_size-1) # 递归左子树
        root.right = self.treeBuild(postorder,inorder,hash_dic,inorder_index+1,inorder_right,postorder_left+left_size,postorder_right-1) # 递归右子树
        return root
        
# @lc code=end

