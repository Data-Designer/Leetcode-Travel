#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/') # list
        res = []
        for i in path:
            if not i:
                continue
            res.append(i)
        # [a b c d . . ..]
        paths = []
        for i in res:
            if i not in ['.','..']:
                paths.append(i)
                # 实际上.是没有pop的
            # elif i == '.':
            #     if paths:
            #         # paths.pop()
            #         pass
            elif i == '..':
                if paths:
                    paths.pop() 
        ans = '/'+'/'.join(paths)
        return ans




# @lc code=end

