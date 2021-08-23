'''
Description: 有向无环图，DAG，BFS
version: 
Author: Data Designer
Date: 2021-08-23 10:25:52
LastEditors: Data Designer
LastEditTime: 2021-08-23 11:04:42
'''
#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 初始化
        indegrees = [0] * numCourses
        adj = [[] for _ in range(numCourses)] # 这里不能直接相乘 
        for cur,pre in prerequisites:
            # 更新邻接表和入度
            indegrees[cur] +=1
            adj[pre].append(cur)
        from collections import deque
        queue = deque()
        for i in range(len(indegrees)):
            if not indegrees[i] :
                queue.append(i) # 存的是节点
        while queue:
            pre = queue.popleft() # 这里上的是先修课
            numCourses -=1
            for cur in adj[pre]:
                indegrees[cur] -=1
                if not indegrees[cur]:
                    queue.append(cur)
        return not numCourses
# @lc code=end

