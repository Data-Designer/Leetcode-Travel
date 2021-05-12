'''
Description: 
version: 
Author: Data Designer
Date: 2021-05-08 13:03:00
LastEditors: Data Designer
LastEditTime: 2021-05-08 13:40:41
'''
#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # dic = {i:chr(64+i) for i in range(1,27)}
        res = ""
        while columnNumber:
            columnNumber = columnNumber - 1
            res = chr(columnNumber % 26 + 65) + res
            columnNumber = columnNumber // 26
        return res
# @lc code=end

