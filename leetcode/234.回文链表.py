'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-15 23:46:48
LastEditors: Data Designer
LastEditTime: 2021-04-15 23:53:45
'''
#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        if res == list(reversed(res)):
            return True
        else:
            return False # 或者新建一个链表
# @lc code=end

