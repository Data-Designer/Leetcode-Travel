'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-22 21:16:47
LastEditors: Data Designer
LastEditTime: 2021-04-22 21:40:15
'''
#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        A = headA
        B = headB
        while A != B:
            A = A.next if A else headB # 手拉手一起走
            B = B.next if B else headA
        return A



# @lc code=end

