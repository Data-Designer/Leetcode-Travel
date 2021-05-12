'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-28 21:00:13
LastEditors: Data Designer
LastEditTime: 2021-03-28 21:14:55
'''
#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        next_head = head.next
        head.next = self.swapPairs(next_head.next)
        next_head.next = head # 递归
        return next_head

        
        
# @lc code=end

