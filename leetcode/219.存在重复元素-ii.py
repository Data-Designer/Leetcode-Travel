'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-26 12:32:20
LastEditors: Data Designer
LastEditTime: 2021-04-26 12:57:42
'''
#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        size = len(nums)
        hash = {}
        for i in range(size):
            if nums[i] not in hash:
                hash[nums[i]] = i # 索引是值
            else:
                if i-hash[nums[i]]<=k:
                    return True
                else:
                    hash[nums[i]] = i # 这里存储靠后的index
        return False
        
# @lc code=end

