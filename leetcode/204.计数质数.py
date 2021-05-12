'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-23 22:04:41
LastEditors: Data Designer
LastEditTime: 2021-04-27 22:31:01
'''
#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3:
            return 0
        else:
            out = [1]*n
            out[0],out[1] = 0,0
            for i in range(2,int(n**0.5)+1):
                # 为什么是根号n，因为必有大于和小于N的因子
                if out[i]==1:
                    # 为什么不从2*i开始，因为这个肯定被2的倍数滤掉了，其他同理
                    m = i**2
                    while m<n:
                        out[m] = 0
                        m += i # 所有i的倍数
            return sum(out)
# @lc code=end

