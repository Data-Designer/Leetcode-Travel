'''
Description: 
version: 
Author: Data Designer
Date: 2020-12-20 13:29:52
LastEditors: Data Designer
LastEditTime: 2020-12-20 15:01:17
'''
#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # # 检验行
        # import collections
        # for i in range(len(board[0])):
        #     count = collections.Counter(board[i]) 
        #     for j in range(1,10):
        #         if count[str(j)]>1:
        #             return False
        # # 检验列
        # for i in range(len(board[0])):
        #     column = []
        #     for j in range(len(board[0])):
        #         column.append(board[j][i])
        #     count = collections.Counter(column)
        #     for n in range(1,10):
        #         if count[str(n)]>1:
        #             return False
        # # 检验三宫格
        # ans = [] # 这里会造成严重的id相等的情况test = [[[1]]*3]*3
        # for i in range(3):
        #     ans.append([])
        # for i in ans:
        #     for i in range(3):
        #         ans[i].append([])
        # print(ans)
        # for i in range(len(board)):
        #     for j in range(len(board)):
        #         row = (i+1)//3
        #         column = (j+1)//3
        #         ans[row-1][column-1].extend(board[i][j])
        # for i in range(3):
        #     for j in range(3):
        #         count = collections.Counter(ans[i][j])
        #         for n in range(1,10):
        #             if count[str(n)]>1:
        #                 return False
        # print(ans)
        # return True
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        box = [{} for i in range(9)] # 一般字典和get配合使用
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num!='.':
                    num = int(num)
                    box_id = (i//3)*3+j//3 # 这个其实可以看出来！！！
                    rows[i][num] = rows[i].get(num,0)+1
                    columns[j][num] = columns[j].get(num,0)+1 # get方法很漂亮
                    box[box_id][num] = box[box_id].get(num,0)+1
                    if rows[i][num]>1 or columns[j][num]>1 or box[box_id][num]>1:
                        return False
        return True
        
                

# @lc code=end

