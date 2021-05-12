#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        size = 0
        dummy = head
        while dummy.next:
            size = size+1
            dummy = dummy.next # 这里获得大小
        k = k % (size+1)
        if k == 0:
            return head # 真正的k在这里
        slow = head
        fast = head
        for i in range(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next # k+1处
        heads = slow.next # 问题就出在这个next
        slow.next = None
        fast.next = head
        return heads
# @lc code=end

