'''
Description: 派数据大小的问题
version: 
Author: Data Designer
Date: 2020-12-10 13:39:27
LastEditors: Data Designer
LastEditTime: 2020-12-10 15:10:48
'''
#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if not nums:
        #     return []
        # if sorted(nums,reverse=True)==nums:
        #     return sorted(nums)
        # max_num = 0
        # change = 0
        # for i in range(len(nums)):
        #     if nums[max_num]<=nums[i]:
        #         max_num +=1
        #     else:
        #         change = i
        # if max_num == len(nums):
        #     nums[change],nums[max_num-1] = nums[max_num-1],nums[change]
        # else:
        #     nums[change],nums[max_num] = nums[max_num],nums[change]
        n = len(nums)
        index = 0
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]: #[j,end]降序
                index = i
                break
        
        if index == 0:
            self.reverseFunction(nums, index, n) # 两种特殊情况
        elif index == n-1:
            nums[index], nums[index-1] = nums[index-1], nums[index]
        else:
            for j in range(n-1, index-1, -1): # 找到第一个比index-1大的数字和其交换
                if nums[j] > nums[index-1]:
                    nums[index-1], nums[j] = nums[j], nums[index-1]
                    break
            self.reverseFunction(nums, index, n) # 需要对index后面
    
    def reverseFunction(self, nums, start, end): # 进行排序
        mid = (start+end) // 2
        j = end-1
        for i in range(start, mid):
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1

# @lc code=end

