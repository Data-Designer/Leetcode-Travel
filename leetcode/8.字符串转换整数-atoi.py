'''
Description: 
version: 
Author: Data Designer
Date: 2020-10-26 16:17:35
LastEditors: Data Designer
LastEditTime: 2020-10-26 17:47:41
'''
#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        # 正则表达式的复习
        s = s.lstrip()
        INT_MIN = -2**31
        INT_MAX = 2**31
        mode = r'^[\+\-]?\d+' # 设置规则
        import re
        pattern = re.compile(mode) #先编译
        ans = re.findall(pattern,s)
        ans = int(*ans) # 返回是个列表，进行解包
        return min(max(INT_MIN,ans),INT_MAX-1)
        

            
# @lc code=end

