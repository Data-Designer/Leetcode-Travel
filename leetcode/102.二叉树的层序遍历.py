#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        import collections
        res = []
        # 维护一个队列，保存一次结果
        queue = collections.deque()
        queue.append(root)
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
                res.append(level)
        return res
            
        
        

# @lc code=end

