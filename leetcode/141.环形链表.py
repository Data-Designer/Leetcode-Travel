'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-05 21:15:09
LastEditors: Data Designer
LastEditTime: 2021-04-05 21:37:18
'''
#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next: # 快慢指针
                return False
            else:
                fast = fast.next.next # 最后会指向none
                slow = slow.next
        return True
# @lc code=end

