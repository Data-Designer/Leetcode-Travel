'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-09 21:57:21
LastEditors: Data Designer
LastEditTime: 2021-03-09 23:29:18
'''
#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # p1 = l1
        # p2 = l2 # 先指定两个头指针
        # new_lis = ListNode("") # 指定新链表
        # res = new_lis
        # while p1 and p2:
        #     if p1.val>p2.val:
        #         res.next = p2
        #         p2 = p2.next
        #     else:
        #         res.next = p1
        #         p1 = p1.next
        #     res = res.next
        # res.next = l1 if l1 is not None else l2 # 直接接到后面
        # return new_lis.n
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            # 不确定返回l2时候反向思考,l2.next = None,则前面最大的应该是l1,比这个l1小的就是前面的l2
            l2.next =  self.mergeTwoLists(l1,l2.next)
            return l2
        else:
            l1.next =  self.mergeTwoLists(l1.next,l2)
            return l1


# @lc code=end

