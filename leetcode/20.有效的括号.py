#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'}':'{',']':'[',')':'('}
        stack = [] # 一定要有动态思维，匹配的已经出栈了
        for i in s:
            if stack and i in dic: # i是右括号
                if dic[i]==stack[-1]: # 如果栈顶是对应左括号
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack
                
# @lc code=end

