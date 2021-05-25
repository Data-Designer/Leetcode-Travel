'''
Description: 快慢指针，找中点，递归
version: 
Author: Data Designer
Date: 2021-05-25 09:24:33
LastEditors: Data Designer
LastEditTime: 2021-05-25 09:40:54
'''
#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        elif not head.next:
            return TreeNode(head.val)

        slow, fast = head, head
        while fast and fast.next:
            pre = slow # 指向slow的前一个节点
            slow = slow.next
            fast = fast.next.next
        pre.next = None # 拆分链表
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next) # slow后面的节点
        return root



# @lc code=end

