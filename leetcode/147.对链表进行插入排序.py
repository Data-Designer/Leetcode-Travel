'''
Description: pre搜寻和cur = lastNode.next
version: 
Author: Data Designer
Date: 2021-06-06 18:23:22
LastEditors: Data Designer
LastEditTime: 2021-06-06 18:39:02
'''
#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        last_node = head
        cur = head.next
        while cur:
            if last_node.val<=cur.val:
                last_node = last_node.next
            else:
                pre = dummy
                while pre.next.val <=cur.val:
                    pre = pre.next
                # 终于找到第一个比cur大的数,注意顺序
                last_node.next = cur.next
                cur.next = pre.next
                pre.next = cur
            cur = last_node.next
        return dummy.next
        
# @lc code=end

