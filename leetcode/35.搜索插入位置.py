'''
Description: 
version: 
Author: Data Designer
Date: 2020-11-05 21:44:20
LastEditors: Data Designer
LastEditTime: 2020-11-05 22:26:59
'''
#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 好像也可以采取左边界检测的办法
        if not nums:
            return 0
        left,right = 0,len(nums)-1
        if nums[0] == target:
            # 如果只有一个数
            return 0
        while left<right:
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
        if nums[left]>target: #直接替代原来的left而不用-1
            return max(left,0)
        elif nums[left]==target:
            return left
        else:
            return left+1



'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        if target<nums[0]:
            return 0
        elif target>nums[-1]:
            return len(nums)
        else:
            l,r=0,len(nums)-1
            while l<r:
                mid=l+(r-l)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            if nums[l]<target:
                return l+1
            else:
                return l

作者：Jamiechen_sjtu
链接：https://leetcode-cn.com/problems/search-insert-position/solution/er-fen-fa-qing-song-gao-ding-by-jamiechen_sjtu-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
# @lc code=end

