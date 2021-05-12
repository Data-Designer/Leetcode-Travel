'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-07 16:16:41
LastEditors: Data Designer
LastEditTime: 2021-03-07 17:30:45
'''
#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        slow = ListNode(None) # 只是为了指针类型
        slow.next = head
        fast = slow
        for i in range(n):
            fast = fast.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        if slow.next == head:
            # 判断是否是头节点
            head = head.next
        else:
            slow.next = slow.next.next
        return head
# @lc code=end

