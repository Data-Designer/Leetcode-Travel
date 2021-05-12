'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-07 12:24:39
LastEditors: Data Designer
LastEditTime: 2021-03-07 13:41:52
'''
#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        # 两个指针检测
        c1 = 0
        c2 = 1
        size = len(s)
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,
        'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        if size == 1:
            # 只有一个
            return dic[s]
        res = 0
        while c2 <= size-1:
            # 先检测是否有现成的
            if s[c1]+s[c2] in dic.keys():
                res = res + dic[s[c1]+s[c2]]
                c1 = c2 +  1
                c2 = c2 + 2
            elif c2+1<=size-1 and s[c2] + s[c2+1] in dic.keys():
                # 这种是跨阈,需要不越界
                res = res + dic[s[c1]] + dic[s[c2]+s[c2+1]]
                c1 = c2 + 2
                c2 = c2 + 3
            else:
                res = res + dic[s[c1]] + dic[s[c2]]
                c1 = c2 +  1
                c2 = c2 + 2
            print(res)
        if c1 == size-1:
            # 最后未能成对
            res = res+ dic[s[-1]]    

        return res

# @lc code=end

