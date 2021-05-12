'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-12 23:09:40
LastEditors: Data Designer
LastEditTime: 2021-04-12 23:37:30
'''
#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        # 先返回特殊情况
        if not root:
            return []
        res = []
        self.dfs(root,targetSum,[],res)
        return res # 不能设置为全局变量！不然会一直留存
        
    def dfs(self,root,targetSum,path,res):
        if not root:
            return []
        if not root.left and not root.right:
            if root.val == targetSum: # 叶子节点和剩余值
                res.append(path+[root.val]) # 别忘了叶子节点
        self.dfs(root.left, targetSum-root.val, path+[root.val], res)
        self.dfs(root.right, targetSum-root.val, path+[root.val], res)

# @lc code=end

