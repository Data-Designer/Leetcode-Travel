'''
Description: 快排，堆排序，归并排序都是O(nlgn)
version: 
Author: Data Designer
Date: 2021-06-07 09:02:11
LastEditors: Data Designer
LastEditTime: 2021-06-07 09:26:50
'''
#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: # 终止条件，因为快慢指针
            return head
        # 归并排序
        slow = head
        fast = head.next
        # 快慢指针找中点
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid,slow.next = slow.next,None
        # 递归
        left,right = self.sortList(head),self.sortList(mid)
        # 下面遍历排序
        res=h=ListNode(0) # 指向同一块内存
        while left and right:
            if left.val <=right.val:
                h.next,left = left,left.next
            else:
                h.next,right = right,right.next
            h = h.next
        # 下面遍历剩余
        h.next = left if left else right
        return res.next
            
            
# @lc code=end

