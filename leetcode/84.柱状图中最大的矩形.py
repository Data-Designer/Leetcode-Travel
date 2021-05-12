#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 主要是面积的计算方法，每一个i对应的最大面积就是(right-left-1)*height[i]
        # res = 0
        # n = len(heights)
        # for i in range(n):
        #     left_i = i
        #     right_i = i
        #     while left_i >= 0 and heights[left_i] >= heights[i]:
        #         left_i -= 1
        #     while right_i < n and heights[right_i] >= heights[i]:
        #         right_i += 1
        #     res = max(res, (right_i - left_i - 1) * heights[i])
        # return res
        # 单调栈
        stack = []
        heights = [0] + heights + [0] # 处理边界问题
        res = 0
        for i in range(len(heights)):
            #print(stack)
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop() #b
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i) # 存储
        return res
            

# @lc code=end

