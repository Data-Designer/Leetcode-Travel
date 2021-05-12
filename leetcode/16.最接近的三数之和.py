#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # nums.sort()
        # k = 0
        # res = 10000000
        # if len(nums)==3:
        #     return nums[0] + nums[1] + nums[2]
        # for k in range(0,len(nums)-2):
        #     i,j = k+1,len(nums)-1
        #     while i<j:
        #         s = nums[k]+nums[i]+nums[j]
        #         if s>target:
        #             j = j-1
        #             res = min(s-target,abs(res))
        #         elif s<target:
        #             i=i+1
        #             res = min(target-s,abs(res))*(s-target)/abs(s-target)
        #         else:
        #             return target
        # # 这里res是和target的差值
        # return int(res+target)
        if len(nums)==3:
            return sum(nums)
        d = float(inf)
        nums.sort()
        ans= 0
        for k in range(len(nums)):
            i,j = k+1,len(nums)-1
            while i<j:
                s = nums[i]+nums[k]+nums[j]-target
                if abs(s)<d:
                    d = abs(s)
                    ans = nums[i]+nums[k]+nums[j]
                if s>0:
                    j = j-1 # need lower
                elif s<0:
                    i = i+1
                else:
                    return target
        return ans

                                
# @lc code=end

