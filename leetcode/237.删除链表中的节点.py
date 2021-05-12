'''
Description: 
version: 
Author: Data Designer
Date: 2021-05-05 12:36:24
LastEditors: Data Designer
LastEditTime: 2021-05-05 12:46:15
'''
#
# @lc app=leetcode.cn id=237 lang=python3
#
# [237] 删除链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # pre = head
        # cur = head.next # 指向头节点
        # while cur.next:
        #     if cur.val == node:
        #         pre.next =cur.next
        #         cur = cur.next
        #     pre = pre.next
        #     cur = cur.next
        # return head.next
        node.val = node.next.val # 变换
        node.next = node.next.next
        
# @lc code=end

