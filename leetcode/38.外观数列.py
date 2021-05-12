'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-08 09:03:22
LastEditors: Data Designer
LastEditTime: 2021-03-29 20:27:27
'''
#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        pre = '' # 前一个样本
        cur = '1'
        for i in range(1,n): # 为1时候压根不遍历
            pre = cur
            cur = ''
            start = 0 # 遍历pre样本
            end = 0
            while end < len(pre):
                while end<len(pre) and pre[end]==pre[start]: #判断在前
                    end = end + 1
                cur += str(end-start)+pre[start]
                start = end # 遍历下一个子块
        return cur

# @lc code=end

