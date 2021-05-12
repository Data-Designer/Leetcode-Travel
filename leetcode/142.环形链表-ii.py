'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-10 11:41:02
LastEditors: Data Designer
LastEditTime: 2021-04-10 12:39:03
'''
#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        fast = head
        slow = head
        pre = head
        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next # 走两步
            else:
                return None
            if fast == slow:
                while pre != slow:
                    slow = slow.next
                    pre = pre.next
                return pre
        return None # 刚刚那个解法应该也是没跳出循环的问题
        
        
# @lc code=end

