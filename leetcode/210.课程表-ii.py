'''
Description: BFS
version: 
Author: Data Designer
Date: 2021-08-23 11:05:23
LastEditors: Data Designer
LastEditTime: 2021-08-23 11:11:48
'''
#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            indegrees[cur] +=1
            adj[pre].append(cur)
        from collections import deque
        queue = deque()
        for i in range(len(indegrees)):
            if not indegrees[i]:
                queue.append(i) # 存储节点
        res = []
        while queue:
            pre = queue.popleft()
            res.append(pre)
            numCourses -= 1
            for cur in adj[pre]:
                indegrees[cur]-=1
                if not indegrees[cur]:
                    queue.append(cur)
        return res if not numCourses else []


# @lc code=end

