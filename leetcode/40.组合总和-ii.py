'''
Description: 
version: 
Author: Data Designer
Date: 2020-12-14 23:40:44
LastEditors: Data Designer
LastEditTime: 2020-12-15 09:28:41
'''
#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates.sort()
        if target< candidates[0]:
            return []
        n = len(candidates)
        res = []
        path = []
        self.dfs(res,path,n,candidates,0,target)
        return res
    
    def dfs(self,res,path,size,candidates,begin,target):
        # if target<0:
        #     return 
        if target==0:
            res.append(path)
        for index in range(begin,size):
            if candidates[index] > target: # 剩余的第一个路径都比target大就没必要剪了
                break
            if index>begin and candidates[index-1]==candidates[index]: # 同层和前一个节点相同的值就没必要搜了
                continue
            self.dfs(res,path+[candidates[index]],size,candidates,index+1,target-candidates[index])
            
    # def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    #     size = len(candidates)
    #     if size == 0:
    #         return []
    #     candidates.sort()
    #     res = []
    #     self.dfs(0, [], target,size,candidates,res)
    #     return res


    # def dfs(self,begin, path, residue,size,candidates,res):
    #     if residue == 0:
    #         res.append(path[:])
    #         return

    #     for index in range(begin, size):
    #         if candidates[index] > residue: # 因为排好序了，若第一个candidats较大，则无需搜索了
    #             break

    #         if index > begin and candidates[index - 1] == candidates[index]:
    #             continue # 同层相同节点也不要搜索了

    #         path.append(candidates[index])
    #         self.dfs(index + 1, path, residue - candidates[index],size,candidates,res)
    #         path.pop()

            
# @lc code=end

