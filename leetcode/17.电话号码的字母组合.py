'''
Description: 
version: 
Author: Data Designer
Date: 2020-11-06 23:32:06
LastEditors: Data Designer
LastEditTime: 2020-11-07 16:54:01
'''
#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2':'abc',
               '3':'def',
               '4':'ghi',
               '5':'jkl',
               '6':'mno',
               '7':'pqrs',
               '8':'tuv',
               '9':'wxyz'}
        if digits=="":
            return []
        # 感觉像广度遍历
        import collections
        q = collections.deque() # 暂存中间结果
        q.append('')
        for i in range(len(digits)):
            # 遍历每个数字
            len_q = len(q)
            for j in range(len_q):
                # 遍历每个中间结果
                cur_digit = dic[digits[i]] # 查找key->value
                cur_m = q.popleft() # 取出中间结果
                for k in cur_digit:
                    q.append(cur_m+k)
        return list(q)
            


                
# @lc code=end

