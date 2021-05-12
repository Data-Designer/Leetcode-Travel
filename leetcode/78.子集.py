'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-16 19:03:47
LastEditors: Data Designer
LastEditTime: 2021-03-16 20:34:56
'''
#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         self.res = [] # 这里需要在下一个函数中使用
#         self.backtrack([],nums,0)
#         return self.res

#     def backtrack(self,tmp, nums,index):
#         # tmp就是一次搜索的结果
#         if index == len(nums):
#             if tmp:
#                 self.res.append(tmp)
#             return
#         # 这里就一次遍历就结束了，我们只需要leaf的结果
#         # 加入元素
#         self.res.append(self.backtrack(tmp + [nums[index]],nums,index+1))
#         self.res.append(self.backtrack(tmp,nums,index+1)) # 不加入该元素
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], 0, nums)
        return self.res
        
    def backtrack(self, sol, index, nums):
        if index == len(nums):
            self.res.append(sol)
            return
        
        self.backtrack(sol+[nums[index]], index+1, nums)
        self.backtrack(sol, index+1, nums) # 这个index顺序为什么会有影响？
# @lc code=end

