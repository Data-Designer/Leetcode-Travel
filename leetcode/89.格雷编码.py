'''
Description: G(n)倒叙R(n)，前面加一，然后合并
version: 
Author: Data Designer
Date: 2021-05-21 09:59:23
LastEditors: Data Designer
LastEditTime: 2021-05-21 10:02:17
'''
#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        head = 1
        for i in range(n):
            for j in range(len(res)-1,-1,-1): # 倒叙保证位数差一
                res.append(res[j]+head) # 加入R(n)
            head = head << 1
        return res

        
# @lc code=end

