'''
Description: root.left.next = root.next.right为核心代码
version: 
Author: Data Designer
Date: 2021-05-27 10:18:25
LastEditors: Data Designer
LastEditTime: 2021-05-27 10:24:49
'''
#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root # 这种方法比较好
        pre = root # 指向每一层的首结点
        while pre.left: # 不然就不是完美二叉树；
            tmp = pre # 用于做串联
            while tmp:
                tmp.left.next = tmp.right
                if tmp.next: # 第一层是空的,从第二层开始看
                    tmp.right.next = tmp.next.left
                tmp = tmp.next # 在一层内循环
            pre = pre.left
        return root

if __name__ == "__main__": #可以用于调试
    print("Hello world")
        
# @lc code=end

