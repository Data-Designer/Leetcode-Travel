'''
Description: # 字典，按长度进行存储，匹配相同长度的单词
version: 
Author: Data Designer
Date: 2021-08-27 09:13:06
LastEditors: Data Designer
LastEditTime: 2021-08-27 09:38:29
'''
#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#

# @lc code=start
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections
        self.dic = collections.defaultdict(list)


    def addWord(self, word: str) -> None:
        size = len(word)
        self.dic[size].append(word) # +=[word]


    def search(self, word: str) -> bool:
        size = len(word)
        def match(same_len_word):
            for i in range(size):
                if word[i] not in {'.',same_len_word[i]}:
                    return False
            return True
        for same_len_word in self.dic[size]:
            if match(same_len_word):
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

