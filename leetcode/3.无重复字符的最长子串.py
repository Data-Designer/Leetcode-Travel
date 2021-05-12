'''
Description: 
version: 
Author: Data Designer
Date: 2020-12-09 15:35:03
LastEditors: Data Designer
LastEditTime: 2020-12-09 16:27:07
'''
#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 暴力
        # ans = 1
        # if len(s)==0:
        #     return 0
        # if len(s)==1:
        #     return ans
        # for i in range(len(s)):
        #     if i>0 and s[i]==s[i-1]:
        #         continue
        #     j = i
        #     while j<len(s) and len(set(list(s[i:j])))==len(list(s[i:j])):
        #         j = j+1
        #     if j<len(s) and len(set(list(s[i:j])))!=len(list(s[i:j])):
        #         temp_ans = len(list(s[i:j-1]))
        #         ans = max(temp_ans,ans)
        #     else :
        #         temp_ans = len(list(s[i:j]))
        #         ans = max(temp_ans,ans)
        # return ans
        # 采用滑动窗口
        win = set()
        ans = 0
        n = len(s)
        q = -1 # 指针
        if len(s)==0:
            return 0
        for i in range(n):
            if i >0:
                win.remove(s[i-1]) # 窗口滑动
            while q+1<n and s[q+1] not in win:
                win.add(s[q+1])
                q = q+1
            ans = max(ans,len(win))
        return ans 



# @lc code=end

