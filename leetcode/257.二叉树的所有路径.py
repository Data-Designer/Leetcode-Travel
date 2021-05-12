#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        self.dfs(root,'',res)
        return res

    def dfs(self,root,path,res):
        if root:
            path = path + str(root.val) # 不能自动类型转换
            # 如果是叶子节点
            if not root.left and not root.right:
                res.append(path)
                return # 不加return心理难受
            else:
                path += '->'
                self.dfs(root.left,path,res)
                self.dfs(root.right,path,res)
        

# @lc code=end

