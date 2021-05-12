'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-06 21:49:28
LastEditors: Data Designer
LastEditTime: 2021-04-06 22:02:13
'''
#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in numbers:
            if target-i in numbers: # 双执政
                if target-i != i:
                    return sorted([numbers.index(i)+1,numbers.index(target-i)+1])
                else:
                    return sorted([numbers.index(i)+1,numbers.index(i)+2])
# @lc code=end

