'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-21 21:04:17
LastEditors: Data Designer
LastEditTime: 2021-04-21 21:15:31
'''
#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle = columnTitle[::-1]
        AZ_string = {chr(i):i-64 for i in range(65, 91)} # 这个要学习一下
        res = 0
        for index,char in enumerate(columnTitle):
            res = res + pow(26,index)*AZ_string[char]
        return res
        

# @lc code=end

