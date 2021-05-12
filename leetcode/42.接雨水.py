#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # 暴力解法
        # ans =0
        # for i in range(len(height)):
        #     max_left  = 0
        #     for j in range(i):
        #         # 寻找max left
        #         if height[j]> max_left:
        #             max_left = height[j]
        #     max_right = 0
        #     for n in range(i+1,len(height)):
        #         if height[n]>max_right:
        #             max_right = height[n]
        #     if min(max_left,max_right)>height[i]:
        #         ans += min(max_left,max_right)-height[i]

        # return ans
        # 重点在于一个单元格一个单元格的思考，要假设水不会侧漏！
        # 一个格子是否能接到水是由其左右最大最小边决定的
        ans = 0
        if not height:
            return 0
        left,right = 0,len(height)-1
        max_left = height[left]
        max_right = height[right]
        while left <right:
            max_left = max(height[left],max_left)
            max_right = max(height[right],max_right)
            if max_left<max_right:
                ans += max_left-height[left] # 始终用短边去减
                left = left +1
            else:
                ans+= max_right -height[right]
                right = right-1
        return ans





# @lc code=end

