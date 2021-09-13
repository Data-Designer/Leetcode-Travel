'''
Description: 双向链表+哈希表
version: 
Author: Data Designer
Date: 2021-09-13 12:32:49
LastEditors: Data Designer
LastEditTime: 2021-09-13 15:35:05
'''
#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#

# @lc code=start
class Node:
    def __init__(self,key,val,pre=None,next=None) -> None:
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next
    

class Double:
    """构造双向链表"""
    def __init__(self) -> None:
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0 

    def addFirst(self,x):
        # 将x插入链表开头
        x.next = self.head.next
        x.pre = self.head
        self.head.next.pre = x
        self.head.next = x
        self.size +=1

    def remove(self,x):
        # 此时x一定存在
        x.pre.next = x.next
        x.next.pre = x.pre
        self.size -= 1

    def removeLast(self):
        if self.size == 0:
            return None
        last_node = self.tail.pre 
        self.remove(last_node)
        return last_node
    
    def getSize(self):
        return self.size



class LRUCache:

    def __init__(self, capacity: int):
        self.map = {} # Hash Table,查找快
        self.cache = Double()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in  self.map: # 直接查找
            return -1
        else:
            val = self.map[key].val
            self.put(key,val) # 节点提前
            return val
        
    def put(self, key: int, value: int) -> None:
        new_item = Node(key,value)
        if key in self.map: # 字典这么做就行
            self.cache.remove(self.map[key]) # 删掉旧数据
            self.cache.addFirst(new_item) # 插入开头
            self.map[key] = new_item # 更新
        else:
            if self.cache.getSize() == self.capacity: # 满了
                last_node = self.cache.removeLast() # 删除最后一个数据位置
                self.map.pop(last_node.key) # 删除映射关系
            self.cache.addFirst(new_item) # 插入开头（满了不满都要插入）
            self.map[key] = new_item # 添加对新节点的映射
        
                    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

