'''
Description: 
version: 
Author: Data Designer
Date: 2020-10-26 15:39:33
LastEditors: Data Designer
LastEditTime: 2020-10-26 16:05:11
'''
#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''哨兵和游标的思想'''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p_head=p=ListNode(None) # 指向同一个对象
        s = 0
        while l1 or l2 or s: # 顺带就搞定了不等情况
            s += (l1.val if l1 else 0)+(l2.val if l2 else 0)
            p.next = ListNode(s%10) # 注意需要使用ListNode的格式，不然会报错
            s = s//10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            p = p.next
        return p_head.next


# @lc code=end

