'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-22 21:40:49
LastEditors: Data Designer
LastEditTime: 2021-04-22 21:45:57
'''
#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = dummy.next
        while cur:
            next = cur.next
            if cur.val==val:
                pre.next = next
                cur = next
            else:
                pre = cur
                cur = next
        return dummy.next
                


# @lc code=end

