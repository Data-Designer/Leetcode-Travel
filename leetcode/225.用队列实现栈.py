'''
Description: 
version: 
Author: Data Designer
Date: 2021-05-06 21:57:35
LastEditors: Data Designer
LastEditTime: 2021-05-06 22:04:02
'''
#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lis = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.lis.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        popp = self.lis.pop()
        return popp


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.lis[-1]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.lis == []



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

