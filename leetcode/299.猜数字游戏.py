'''
Description: 两个数组,取交集
version: 
Author: Data Designer
Date: 2021-05-30 20:59:10
LastEditors: Data Designer
LastEditTime: 2021-05-30 21:24:16
'''
#
# @lc app=leetcode.cn id=299 lang=python3
#
# [299] 猜数字游戏
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # bulls = 0
        # from collections import defaultdict
        # cows = defaultdict(int)
        # cows_num = 0
        # size = len(secret)
        # bull_str = ""
        # for i in range(size):
        #     if secret[i] == guess[i]:
        #         bulls +=1
        #     else:
        #         cows[secret[i]] += 1 # 这里存储真实数字的hash
        #         bull_str = bull_str + guess[i] # 只有没有匹配上bull的才参与cow
        # for i in range(len(bull_str)):
        #     if bull_str[i] in cows:
        #         cows_num +=1
        #         # cows[i] -=1 是字符不能重复计算
        #         cows.pop(bull_str[i])
        bulls = 0
        cows = 0
        from collections import Counter
        bulls = sum(s==g for s,g in zip(secret,guess))
        cows = sum((Counter(secret) & Counter(guess)).values())-bulls # 需要去掉bull中对应位置出现过的
        return str(bulls) + "A" + str(cows) +"B"
                



# @lc code=end

