'''
Description: 
version: 
Author: Data Designer
Date: 2020-12-12 09:46:42
LastEditors: Data Designer
LastEditTime: 2020-12-12 12:25:15
'''
#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        candidates.sort() # 排序==剪枝
        n = len(candidates)
        if n==0: # 特殊情况
            return []
        # 回溯法，路径是candidates，孩子节点是差值，只要找到最后是0的差值即可
        self.dfs(0,n,candidates,path,res,target)
        return res

    

    def dfs(self,begin,size,candidates,path,res,target):
        if target<0:
            return 
        if target==0: # 只有在path值符合要求才加入res
            res.append(path)
            return
        # if target<candidates[index]: # 强制向后搜索
        #     return 
        for index in range(begin,size): # 每层都是全分裂，target值缩小,这里传入begin的原因是防止前向搜索
            self.dfs(index,size,candidates,path+[candidates[index]],res,target-candidates[index])

        
# @lc code=end

