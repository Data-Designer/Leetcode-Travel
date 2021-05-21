'''
Description: 双链表
version: 
Author: Data Designer
Date: 2021-05-19 21:54:42
LastEditors: Data Designer
LastEditTime: 2021-05-21 09:37:57
'''
#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy_small,dummy_large,head = ListNode(-1),ListNode(-1),head
        small,large,cur = dummy_small,dummy_large,head
        while cur:
            if cur.val < x:
                small.next = cur
                small = small.next
            else:
                large.next = cur
                large = large.next
            cur = cur.next
        large.next=  None # 注意清空！
        small.next = dummy_large.next
        return dummy_small.next
        
# @lc code=end

