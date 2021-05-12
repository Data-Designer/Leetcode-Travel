'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-15 23:18:36
LastEditors: Data Designer
LastEditTime: 2021-04-15 23:41:25
'''
#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # dummy = ListNode()
        # dummy.next = head
        pre = None
        cur = head
        while cur:
            next = cur.next   # 先把原来cur.next位置存起来
            cur.next = pre
            pre = cur
            cur = next
        return pre

# @lc code=end

