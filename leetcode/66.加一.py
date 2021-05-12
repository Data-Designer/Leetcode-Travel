'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-21 19:45:49
LastEditors: Data Designer
LastEditTime: 2021-03-21 20:09:42
'''
#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits)==1 and digits[0]==0:
            return [1]
        flag = 10
        size = len(digits)
        res = 0
        for index,i in enumerate(digits):
            res = res + pow(flag,size-index-1)*i
        res = str(res+1)
        ans = []
        for i in res:
            ans.append(int(i))

        return ans
        
# @lc code=end

