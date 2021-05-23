'''
Description: 卡特兰树，dp，二叉搜索树的构造只需要确定根节点
version: 
Author: Data Designer
Date: 2021-05-23 12:27:10
LastEditors: Data Designer
LastEditTime: 2021-05-23 12:46:49
'''
#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n:
            return []
        res = []
        res = self.build_search_tree(1,n)
        return res
    
    def build_search_tree(self,start,end):
        if start > end:
            return [None,] # 这个终止条件没看懂
        all_res = [] # 存储以某节点为根的树的列表
        for i in range(start,end+1): # 所有的节点作为根节点
            left_search_tree = self.build_search_tree(start,i-1)
            right_search_tree = self.build_search_tree(i+1,end)
            
            # 下面遍历左右子树
            for left in left_search_tree:
                for right in right_search_tree:
                    cur = TreeNode(i)
                    cur.left = left
                    cur.right = right
                    all_res.append(cur)
        return all_res

# @lc code=end

