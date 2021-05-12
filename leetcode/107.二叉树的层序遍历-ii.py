'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-10 15:10:04
LastEditors: Data Designer
LastEditTime: 2021-04-10 15:34:53
'''
#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        #跟结点入queue
        queue = [root]
        res = []
        while queue:
            res.append([node.val for node in queue]) # 每一层的所有值
            #存储当前层的孩子节点列表
            ll = []
            #对当前层的每个节点遍历
            for node in queue:
                #如果左子节点存在，入队列
                if node.left:
                    ll.append(node.left)
                #如果右子节点存在，入队列
                if node.right:
                    ll.append(node.right)
            #后把queue更新成下一层的结点，继续遍历下一层
            queue = ll
        #列表倒序
        return res[::-1]

            
            

# @lc code=end

