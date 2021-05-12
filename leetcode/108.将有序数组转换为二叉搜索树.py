'''
Description: 
version: 
Author: Data Designer
Date: 2021-05-09 18:45:18
LastEditors: Data Designer
LastEditTime: 2021-05-09 19:30:47
'''
#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # 二叉搜索树的中序遍历是递增数组
        # 何时结束
        if not nums:
            return None
        # 递归过程
        mid = len(nums)//2
        root = TreeNode(nums[mid])        
        left = nums[:mid]
        right = nums[mid+1:]
        root.left = self.sortedArrayToBST(left)
        root.right = self.sortedArrayToBST(right)
        # 返回结果
        return root

# @lc code=end

