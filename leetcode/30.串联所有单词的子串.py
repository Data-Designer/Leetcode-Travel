'''
Description: 
version: 
Author: Data Designer
Date: 2020-12-17 10:44:02
LastEditors: Data Designer
LastEditTime: 2020-12-17 14:04:27
'''
#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # 暴力全排
        # que = []
        # que2 = []
        # num = len(words)
        # import itertools
        # que = list(itertools.permutations(words))
        # for mem in que:
        #     que2.append("".join(mem))
        # print(que2)
        # import re
        # index_list = []
        # for mem in que2:
        #     index_list += [i.start() for i in re.finditer(mem,s)]
        # print(index_list)
        # return list(set(index_list))
        # 转化为比较两个Hash table中的词的数量
        if not s or not words:
            return []
        one_word = len(words[0])
        all_len = len(words)*one_word # 前提是单词长度相同
        n = len(s)
        res = []
        from collections import Counter
        hash_dic1 = Counter(words) # 维护单词的Hash表
        for i in range(0,n-all_len+1): # 每次仅比较这个子串
            tmp = s[i:i+all_len]
            c_tmp = [] # 存储每个单词
            for j in range(0,all_len,one_word):
                c_tmp.append(tmp[j:j+one_word])
            if Counter(c_tmp)==hash_dic1:
                res.append(i)
        return res
# s = Solution()
# index_ = s.findSubstring('aaa',['a','a']) 这情况绝了
# print(index_)

# @lc code=end

