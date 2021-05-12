'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-12 09:40:58
LastEditors: Data Designer
LastEditTime: 2021-03-12 10:23:29
'''
#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        from collections import defaultdict
        dic = defaultdict(list) # 创建一个hash table
        for i in range(len(strs)):
            dic[str(sorted(list(strs[i])))].append(strs[i])
        for item in dic.items():
            res.append(item[1])
        return res
# @lc code=end

