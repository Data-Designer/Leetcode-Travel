'''
Description: 第一步，区分正负号，divmod算余数【没有余数的情况】，处理循环使用hash记录位置，只要开始重复就是循环了
version: 
Author: Data Designer
Date: 2021-08-10 21:23:41
LastEditors: Data Designer
LastEditTime: 2021-08-11 09:15:20
'''
#
# @lc app=leetcode.cn id=166 lang=python3
#
# [166] 分数到小数
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = []
        if numerator == 0:
            return '0'
        if (numerator>0) ^ (denominator>0) :
            res.append('-')
        numerator,denominator = abs(numerator),abs(denominator)
        a,b = divmod(numerator,denominator)
        res.append(str(a))
        if b == 0:
            return ''.join(res) # 不能返回0
        res.append('.')
        loc =  {b:len(res)} # 记录位置
        while b:
            b = b*10 # 这是为了除
            a,b = divmod(b,denominator)
            res.append(str(a))
            if b in loc:
                res.insert(loc[b],'(')
                res.append(')')
                break # 这里必须break
            loc[b] = len(res)
        return ''.join(res)
            
# @lc code=end

