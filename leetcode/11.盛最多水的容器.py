'''
Description: 
version: 
Author: Data Designer
Date: 2020-10-16 14:01:59
LastEditors: Data Designer
LastEditTime: 2020-12-09 16:36:20
'''
#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # maxx = 0
        # for i in range(len(height)):
        #     for j in range(1,len(height)):
        #         if min(height[i],height[j])*(j-i)>maxx:
        #             maxx = min(height[i],height[j])*(j-i)
        # return maxx 
        '''
        若向内移动短板，水槽的短板 min(h[i], h[j])min(h[i],h[j]) 可能变大，因此水槽面积 S(i, j)S(i,j) 可能增大。
        若向内移动长板，水槽的短板 min(h[i], h[j])min(h[i],h[j]) 不变或变小，下个水槽的面积一定小于当前水槽面积。
        '''
        i,j = 0,len(height)-1
        res = 0
        while i<j:
            if height[i]<height[j]:
                res = max(res,(j-i)*height[i]) # 移动长板，最小值有可能变得更小
                i +=1
            else:
                res = max(res,(j-i)*height[j])
                j -=1
        return res
        

# @lc code=end

