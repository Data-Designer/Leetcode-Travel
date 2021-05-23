'''
Description: 先序遍历【根【左】【右】】，中序遍历【【左】根【右】】，hash，递归
version: 
Author: Data Designer
Date: 2021-05-23 12:51:44
LastEditors: Data Designer
LastEditTime: 2021-05-23 13:28:03
'''
#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        size = len(preorder)
        hash_dic = {i:index for index,i in enumerate(inorder)} # 因为需要中序遍历确定个数
        return self.treeBuild(preorder,hash_dic,0,size-1,0,size-1)


    def treeBuild(self,preorder,hash_dic,preorder_left,preorder_right,inorder_left,inorder_right):
        if preorder_left > preorder_right: # 终止条件
            return None 
        root = TreeNode(preorder[preorder_left]) # 确定根节点
        inorder_index = hash_dic[preorder[preorder_left]] # 确定根节点位置
        left_size = inorder_index - inorder_left # 左子树数目
        left_tree = self.treeBuild(preorder,hash_dic,preorder_left+1,preorder_left+left_size,inorder_left,inorder_index-1) # 递归构建左子树,注意-1+1，所以不用+1
        right_tree = self.treeBuild(preorder,hash_dic,preorder_left+left_size+1,preorder_right,inorder_index+1,inorder_right)
        root.left = left_tree
        root.right = right_tree
        return root
# @lc code=end

