'''
Description: 
version: 
Author: Data Designer
Date: 2020-11-01 22:30:24
LastEditors: Data Designer
LastEditTime: 2021-05-12 19:04:47
'''
#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        flag = 0 # sign
        # 先考虑符号
        if abs(dividend) + abs(divisor) == abs(dividend+divisor):
            flag = 1
        else:
            flag = -1
        # 被除数较小
        if abs(dividend)<abs(divisor):
            return 0
        elif abs(dividend)==abs(divisor):
            return flag
        # else:
        #     # 使用暴力减法
        #     ans = 0
        #     s = abs(dividend)-abs(divisor)
        #     while s>0:
        #         ans+=1
        #         s -=abs(divisor)
        #     return ans*flag
        else:
            # ans = 1 无法传进闭包
            dividend = abs(dividend)
            divisor = abs(divisor)
            def div(dividend,divisor):
                if dividend < divisor: # 务必加上
                    return 0
                ans = 1
                cur = divisor
                while cur+cur< dividend:
                    cur = cur + cur # 1,2,4倍数
                    ans +=ans
                return ans + div(dividend-cur,divisor) # 有一半是divisor的倍数，几倍也记下来了,然后看不足一半的是divsor的什么倍数
            result = div(dividend,divisor)
        if flag<0:
            result = 0-result
        if result>2**31-1:
            return 2**31-1
        elif result<-2**31:
            return -2**31
        else:
            return result

# @lc code=end

