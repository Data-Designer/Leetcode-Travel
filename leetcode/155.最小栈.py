'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-22 21:09:25
LastEditors: Data Designer
LastEditTime: 2021-04-22 21:12:17
'''
#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.res = []


    def push(self, val: int) -> None:
        self.res.append(val)



    def pop(self) -> None:
        val = self.res.pop()
        return val


    def top(self) -> int:
        return self.res[-1]


    def getMin(self) -> int:
        return min(self.res) # 添加辅助栈



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

