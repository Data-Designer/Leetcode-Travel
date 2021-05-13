'''
Description: 
version: 
Author: Data Designer
Date: 2021-05-13 09:05:48
LastEditors: Data Designer
LastEditTime: 2021-05-13 09:45:40
'''
#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n:
            return []
        res,path = [],[]
        self.backtrack(n,k,1,path,res)
        return res

    def backtrack(self,n,k,index,path,res):
        if k==0: # 明确终止条件
            res.append(path) # 终止条件结束动作
            return
        for i in range(index,n-k+2): # 遍历范围，n-k+1是因为不能超出数组长度，再加1是因为range右开
            # path.append(i),使用append下面要记得pop，这里不用是因为path+[i]产生了新变量
            self.backtrack(n,k-1,i+1,path+[i],res) # +1因为不需要自己,注意不是index+1,是i+1

# @lc code=end

