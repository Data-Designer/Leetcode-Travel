'''
Description: 
version: 
Author: Data Designer
Date: 2021-05-06 22:14:43
LastEditors: Data Designer
LastEditTime: 2021-05-06 22:32:33
'''
#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lis_1 = []
        self.lis_2 = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.lis_1.append(x) # 不用担心为空，只要保证lis_1有就可以了

        



    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.lis_2:
            while self.lis_1:
                self.lis_2.append(self.lis_1.pop())
        return self.lis_2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.lis_2:
            while self.lis_1:
                self.lis_2.append(self.lis_1.pop())
        return self.lis_2[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.lis_1 and not self.lis_2



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

