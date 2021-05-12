#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        import collections
        queue = collections.deque()
        queue.append(root)
        flag = False
        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                if flag:
                    # 务必注意reversed返回的是iter
                    res.append(list(reversed(level)))
                else:
                    res.append(level)
            flag  = not flag
        return res
# @lc code=end

