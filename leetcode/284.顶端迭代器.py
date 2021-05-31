'''
Description: 先存储
version: 
Author: Data Designer
Date: 2021-05-31 09:10:46
LastEditors: Data Designer
LastEditTime: 2021-05-31 09:29:44
'''
#
# @lc app=leetcode.cn id=284 lang=python3
#
# [284] 顶端迭代器
#

# @lc code=start
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

from typing import Iterable, Iterator


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.lis_tmp = []
        self.index = 0
        while iterator.hasNext():
            self.lis_tmp.append(iterator.next())

        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.lis_tmp[self.index]
        

    def next(self):
        """
        :rtype: int
        """
        value = self.lis_tmp[self.index]
        self.index +=1
        return value
            
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index <= len(self.lis_tmp)-1 # 此时还没加
        
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
# @lc code=end

