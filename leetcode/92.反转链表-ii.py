'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-16 00:11:03
LastEditors: Data Designer
LastEditTime: 2021-04-17 22:21:11
'''
#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummyhead = ListNode(-1)
        dummyhead.next = head
        pre = dummyhead
        for i in range(left-1):
            pre = pre.next
        # 此时pre指向待反转的前一个节点
        cur = pre.next # 永远指向第一个节点
        for i in range(right-left):
            next = cur.next # 其实动的是next指针
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        return dummyhead.next




# @lc code=end

