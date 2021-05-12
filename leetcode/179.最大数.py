'''
Description: 
version: 
Author: Data Designer
Date: 2021-03-29 22:52:56
LastEditors: Data Designer
LastEditTime: 2021-03-29 23:21:00
'''
#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # if len(nums)<=0:
        #     return "".join(nums)
        # res = []
        # def backtrack(nums,tmp):
        #     if not nums:
        #         res.append(tmp)
        #         return 
        #     else:
        #         for i in range(len(nums)):
        #             backtrack(nums[:i]+nums[i+1:], tmp+[nums[i]])
        # backtrack(nums, [])
        # max_ = 0
        # for i in res:
        #     ans = ''
        #     for j in i:
        #         ans += str(j)
        #     if int(ans)>max_:
        #         max_ = int(ans)
        # return str(max_)
        from functools import cmp_to_key
        nums = map(str, nums)
        nums = sorted(nums,key = cmp_to_key(self.Large),reverse=True) # 自动针对其进行排序
        ans =  ''.join(nums)
        return str(int(ans))


    def Large(self,x,y):
        if x+y > y+x:
            return 1
        elif y+x>x+y:
            return -1
        else:
            return 0

# @lc code=end

