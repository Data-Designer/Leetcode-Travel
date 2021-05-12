#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        lis = []
        lis = self.dfs(root,lis)
        x = None
        y = None # 用于保留位置，会有两个位置比后一个数大,前面大的是错，后面小的是错的
        pre = lis[0]
        for i in range(1,len(lis)):
            if pre.val>lis[i].val:
                y = lis[i] # 保存后一个位置
                if not x:
                    x = pre # 保存第一个位置
            pre = lis[i]
        if x and y:
            x.val,y.val = y.val,x.val

    def dfs(self,root,lis):
        if not root:
            return 
        self.dfs(root.left,lis)
        lis.append(root)
        self.dfs(root.right,lis)
        return lis
        
# @lc code=end

