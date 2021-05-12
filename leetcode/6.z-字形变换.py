'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-06 20:14:03
LastEditors: Data Designer
LastEditTime: 2021-03-06 23:05:46
'''
#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 先计算有一个矩阵需要多少的数量，构建对应大小的数组
        num = 2 * numRows - 2 # 这个就是一个竖到另一个竖

        # 预判特例
        if num ==0:
            if len(s) <=numRows or numRows==1:
                return s
            else:
                dp = [['' for j in range(numRows)] for i in range(numRows)]
                for i in range(numRows):
                    dp[i][0] = s[i]

                flag = numRows
                flag2 = 1
                for i in range(len(s[numRows:])):
                    dp[numRows-1-i-1][flag2] = s[flag]
                    flag = flag +1
                    flag2 = flag2+1
        numa, numb = len(s)//num ,len(s) % num # 一个是倍数，一个是余数
        # 增加判断，看超过多少
        if numb <= numRows:
            # 多加一列
            dp = [['' for i in range(numa * (numRows-1)+1)] for j in range (numRows)]
        else:
            # 增加好几列
            dp = [['' for i in range(numa * (numRows-1)+numb-numRows+1)] for j in range (numRows)] 
        flag = 0 # 标记s指针
        flag2 = 0 # 标记在哪列
        for flag3 in range(numa):
            # 就直接输出numrows个数字
            for j in range(numRows):
                dp[j][flag2] = s[flag]
                flag += 1 
            flag2 += 1
            
            for j in range(numRows-2):
                dp[numRows-1-j-1][flag2] = s[flag]
                flag += 1
                flag2 += 1
        # 最后剩的不满的，就一组
        if numb<=numRows:
            for i in range(len(s[flag:])):
                dp[i][flag2] = s[flag]
                flag = flag+1
        else:
            for i in range(numRows):
                dp[i][flag2] = s[flag]
                flag = flag+1
            flag2 = flag2+1
            for i in range(len(s[flag:])):
                dp[numRows-1-i-1][flag2] = s[flag]
                flag +=1
                flag2+=1
        res = ""
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                res = res + dp[i][j]
        return res



            
# @lc code=end

