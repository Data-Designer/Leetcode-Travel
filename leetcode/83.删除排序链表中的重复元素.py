'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-06 22:41:38
LastEditors: Data Designer
LastEditTime: 2021-04-06 22:54:13
'''
#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre = head
        cur = head.next
        while cur:
            if pre.val != cur.val:
                pre = pre.next
                cur = cur.next
            else:
                cur = cur.next
                pre.next = cur
        return head

# @lc code=end

