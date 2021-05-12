'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-11 17:16:47
LastEditors: Data Designer
LastEditTime: 2021-03-29 21:28:55
'''
#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        ans = '0'
        m,n = len(num1),len(num2) # 竖乘法
        for i in range(n-1,-1,-1):
            add = 0 # 进位
            curr = ['0'] * (n-i-1) # 补0
            y = int(num2[i])
            for j in range(m-1,-1,-1): # 从后乘！
                tmp = int(num1[j])*y+add
                curr.append(str(tmp % 10)) # 从个位开始补0-9,切记这里str
                add = tmp // 10
            if add > 0:
                curr.append(str(add)) # 最后一位,这里是个列表
            curr = "".join(curr[::-1])
            ans = self.addString(ans,curr)
        return ans


    def addString(self,num1,num2):
        '''需要转换加和'''
        add = 0
        ans = list()
        i,j = len(num1)-1,len(num2)-1
        while i>=0 or j>=0 or add!=0:
            tmp_i = int(num1[i]) if i>=0 else 0
            tmp_j = int(num2[j]) if j>=0 else 0
            tmp = tmp_i + tmp_j + add
            add = tmp // 10
            ans.append(str(tmp % 10))
            i = i-1
            j = j-1
        return "".join(ans[::-1]) # 反过来
        
# @lc code=end

