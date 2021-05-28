'''
Description: 四个指针
version: 
Author: Data Designer
Date: 2021-05-28 09:26:23
LastEditors: Data Designer
LastEditTime: 2021-05-28 09:54:22
'''
#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        pre = root
        while pre:
            cur = pre # 指向当前层头节点
            tail = Node(None) # 用于连接下一层节点
            head = None # 下一层的头节点
            find = False
            while cur: # 遍历当前层节点
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next
                    if not find:
                        head = cur.left
                        find = True
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                    if not find:
                        head = cur.right
                        find = True
                cur = cur.next
            pre = head
        return root


        
# @lc code=end

