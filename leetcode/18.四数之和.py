'''
Description: 
version: 
Author: Data Designer
Date: 2020-12-09 09:35:23
LastEditors: Data Designer
LastEditTime: 2020-12-09 11:01:53
'''
#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # if len(nums)<4:
        #     return []
        # nums_sorted = sorted(nums)
        # i,j = 0,len(nums_sorted)-1
        # ans = []
        # # -2,-1,0,0,1,2
        # if nums_sorted[i]>target or nums_sorted[j]<target:
        #     return []
        # while i<=j-4 and nums_sorted[i]<target and nums_sorted[j]>target:
        #     # 内部双指针
        #     m,n = i+1,j-1
        #     while m<n:
        #         temp = [nums_sorted[i],nums_sorted[j]] # 固定端点，内部搜索
        #         if nums_sorted[m]+nums_sorted[n]==-(nums_sorted[i]+nums_sorted[j]):
        #             temp.append(nums_sorted[m])
        #             temp.append(nums_sorted[n])
        #             ans.append(temp)
        #             m=m+1
        #         elif nums_sorted[m]+nums_sorted[n]>-(nums_sorted[i]+nums_sorted[j]):
        #             n = n-1
        #         else:
        #             m = m+1 
        #     i = i+1
        #     j = j-1
            
        # return ans
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        # 如果最小值的四倍大于target或者最大值的四倍小于target，说明没有满足条件的四数，返回空
        if nums[0]*4>target or nums[-1]*4<target:
            return []
        res = []
        for i in range(n - 3):
            # 在第一层循环中，如果当前元素和前一个相同，去重，跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 如果当前最小的元素的4倍大于target，说明后面没有满足条件的数存在，退出
            if nums[i] * 4 > target:
                break
            
            for j in range(i + 1, n - 2):
                # 在第二层循环中，如果当前元素和前一个相同且前一个元素不为第一层元素，跳过
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l, r = j + 1, n - 1
                # # 当前最大四数之和小于target，继续向后遍历
                # if nums[i] + nums[j] + 2 * nums[r] < target:
                #     continue
                # # 当前最小的四数之和大于target，说明后面没有满足条件的数存在，退出
                # if nums[i] + nums[j] + 2 * nums[l] > target:
                #     break

                while l < r:
                    num = nums[i] + nums[j] + nums[l] + nums[r]
                    if num == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        # 去重，避免相邻数相同
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

                        r -= 1
                        # 去重，避免相邻数相同
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1

                    elif num > target:
                        #四数之和大于target，右指针左移寻找满足条件的较小值
                        r -= 1
                    else:
                        #四数之和小于target，左指针右移寻找满足条件的较大值
                        l += 1
        return res

# @lc code=end

