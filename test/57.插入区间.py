#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
class Solution:
    def insert(self, intervals,newInterval):
        # 这个题目不支持直接排序
        intervals = intervals.append(0)
        for i in range(len(intervals)-1,-1,-1):
            if newInterval[0]<intervals[i][0]:
                intervals[i+1] = intervals[i]
            else:
                break
        intervals[i+1] = newInterval
        res = []
        for i in intervals:
            if len(res)==0 or i[0]>res[-1][1]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1],i[1])
        return res
#         if len(newInterval)==0:
#             return intervals
#         if len(intervals)==0:
#             return [newInterval]
#         intervals = intervals.append(newInterval)
        
#         res = []
#         for i in intervals:
#             if len(res)==0 or i[0]>res[-1][1]: # 如果新进的左区间已经大于res右区间，直接放进去即可
#                 res.append(i)
#             else:
#                 res[-1][1] = max(i[1],res[-1][1])
#         return res
            
# s = Solution()
# res = s.insert([[1,3],[6,9]],[2,5])
# print(res)                
# @lc code=end

