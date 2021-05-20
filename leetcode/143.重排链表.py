'''
Description: 快慢指针，反转链表，链表拼接 
version: 
Author: Data Designer
Date: 2021-05-20 09:37:01
LastEditors: Data Designer
LastEditTime: 2021-05-20 10:07:19
'''
#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 快慢指针
        slow,fast = head,head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        reversed_node = slow.next
        right = self.reverse_(reversed_node) # 反转后面的链表
        slow.next = None # 这里分割为2个链表
        left = head # 左边
        while right: # 拼接,两个链表单指针
            left = left.next
            head.next = right
            head = head.next
            right =  right.next
            head.next = left
            head = head.next

    def reverse_(self,node):
        cur = node
        pre = None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
            
            
# @lc code=end

