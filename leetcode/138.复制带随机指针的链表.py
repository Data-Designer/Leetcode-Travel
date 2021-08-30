'''
Description: hash表,先单纯复制然后再处理random
version: 
Author: Data Designer
Date: 2021-08-30 10:13:31
LastEditors: Data Designer
LastEditTime: 2021-08-30 10:32:23
'''
#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # if not head:
        #     return []
        hashmap = dict()
        dummy = Node(-1)
        tail,tmp = dummy,head
        while tmp:
            node = Node(tmp.val)
            hashmap[tmp] = node # 这个是我没想到的，哈希存储
            tail.next = node
            tail = tail.next
            tmp = tmp.next
        tail,tmp = dummy.next,head
        while tmp:
            if tmp.random:
                tail.random = hashmap[tmp.random] # 指向tmp的random的节点
            else:
                tmp.random = None
            tail = tail.next
            tmp = tmp.next
        return dummy.next
            
# @lc code=end

