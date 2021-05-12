#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 无返回值
        res =[]
        k = 0
        # k<i<j
        
        for k in range(len(nums)-2): # 以k为index
            if nums[k]>0:
                break # k is minest
            if k>0 and nums[k] == nums[k-1]: # [0,0,0]要排除
                continue
            i,j = k+1,len(nums)-1
            while i<j: # double point
                s = nums[k]+nums[i]+nums[j]
                if s<0:
                    i+=1
                    while i<j and nums[i] ==nums[i-1]:
                        i = i+1 # 去重
                elif s>0:
                    j-=1
                    while i<j and nums[j] ==nums[j+1]:
                        j = j-1
                else:
                    res.append([nums[i],nums[j],nums[k]]) # 找到一个
                    i+=1
                    j-=1
                    while i<j and nums[i] ==nums[i-1]: # and和&不能互相替换
                        i=  i+1
                    while i<j and nums[j]==nums[j+1]:
                        j= j-1
        return res  
        
# @lc code=end

