'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-06 22:55:38
LastEditors: Data Designer
LastEditTime: 2021-04-06 23:39:57
'''
#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: # 注意如果是列表一定要先排序
            return head
        dummy = ListNode(0)
        dummy.next = head #有可能删除头节点
        pre = dummy
        cur = head
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if pre.next == cur: # 不存在区间
                pre = pre.next
                cur = cur.next
            else:
                pre.next = cur.next # 但不前进
                cur = cur.next
        return dummy.next


# @lc code=end

