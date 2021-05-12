#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashdict = dict()
        for index1,i in enumerate(nums):
            if target-i in hashdict:
                return [hashdict[target-i],index1]
            hashdict[i] = index1
            
# @lc code=end

