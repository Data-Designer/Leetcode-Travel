'''
Description: 记录起始点,转换数组
version: 
Author: Data Designer
Date: 2021-08-11 20:43:51
LastEditors: Data Designer
LastEditTime: 2021-08-12 19:28:11
'''
#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        # cur = 0 # 目前的油量
        # 这题应该是递归，起点不一样
        N = len(gas) # 一共有多少个加油站
        
        for i in range(N):
            res = self.detect(gas[i:]+gas[:i],cost[i:]+cost[:i])
            if res ==0:
                return i # 返回序号
        return res 

    def detect(self,gas,cost):
        """
        固定起点
        """
        res = 0 # 标志位结果
        cur = 0 # 目前的油量
        for i in range(len(gas)-1):
            cur = cur + gas[i]-cost[i]
            if cur<0:
                res = -1
                return res
        return res
        

# @lc code=end

