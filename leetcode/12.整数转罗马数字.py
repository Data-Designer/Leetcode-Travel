'''
Description: 
version: 
Author: Data Designer
Date: 2020-10-26 17:53:54
LastEditors: Data Designer
LastEditTime: 2021-03-07 12:24:23
'''
#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = self.area(num)
        return res
        
    def area(self,num):
        # 寻找区间
        res = ''
        if num // 1000 !=0:
            # 这些会出现多次
            res = res + 'M'*(num//1000)
            num = num-num//1000 * 1000
        if num // 900 !=0:
            # 这些只会出现一次
            res = res + 'CM'
            num = num - 900
        if num // 500 !=0:
            res = res + 'D'
            num =num -500
        if num //400 !=0:
            res = res + 'CD'*(num//400)
            num =num -num //400 *400
        if num // 100 !=0:
            res = res + 'C'*(num//100)
            num =num-num//100*100
        if num //90 !=0:
            res =res + 'XC'
            num = num-90
        if num // 50 !=0:
            res =res + 'L'
            num = num-50
        if num //40 !=0:
            res = res + 'XL' * (num//40)
            num = num - (num//40)*40
        if num // 10 !=0:
            res = res + 'X'* (num//10)
            num = num - (num//10)*10
        if num // 9 !=0:
            res =res + 'IX'
            num =num-9
        if num //5!=0:
            res = res + 'V'
            num = num -5
        if num // 4!=0:
            res = res + 'IV'*(num//4)
            num = num - (num//4)*4
        if num // 1 !=0:
            res = res + 'I'*(num//1)
            num = num - (num//1)*1
        return res


# @lc code=end

