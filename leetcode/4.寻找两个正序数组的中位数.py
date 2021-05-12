#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num_all = sorted(nums1+nums2)
        if len(num_all)%2==0:
            return (num_all[len(num_all)//2] + num_all[len(num_all)//2-1])/2
        else:
            return num_all[len(num_all)//2] 
# @lc code=end

