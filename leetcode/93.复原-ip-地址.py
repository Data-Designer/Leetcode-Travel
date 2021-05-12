'''
Description: 
version: 
Author: Data Designer
Date: 2021-04-14 23:03:51
LastEditors: Data Designer
LastEditTime: 2021-04-14 23:37:33
'''
#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        size = len(s)
        if size < 4 or size>12:
            return []
        path = [] # 保存每一段
        res = [] # 保存所有有效ip
        self._dfs(s,size,0,0,path,res)
        return res

    def _dfs(self,s,size,split_times,begin,path,res):
        # split_times，切分次数，begin切分指针位置，path切分留存
        if begin==size:
            if split_times ==4:
                res.append('.'.join(path))
            return
        if size - begin < (4-split_times) or size-begin > 3*(4-split_times):
            # 如果剩下的部分小于或者大于最小分割和最大分割
            return
        for i in range(3): #剪枝
            # 每个节点只能截取3种
            if begin + i >= size:
                break # 超出界限就不用了
            ip_segment = self._judge_if_ip_segments(s,begin,begin+i)
            if ip_segment != -1:
                path.append(str(ip_segment)) # 村的是str
                self._dfs(s,size,split_times+1,begin+i+1,path,res) # 多种情况使用for和beigin指针添加，然后继续递归
                path.pop() # 回溯
    def _judge_if_ip_segments(self,s,left,right):
        size = right - left +1
        if size >1 and s[left] == '0':
            return -1
        res = int(s[left:right+1])
        if res > 255:
            return -1
        return res
# @lc code=end

