# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 21:16:45 2021

@author: Anik
"""



class Node(object):
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        
def lca(node1, node2):
    s=set()
    while(node1):
        s.add(node1.value)
        node1=node1.parent
        
    while(node2):
        if node2.value in s:
            return node2.value
        node2=node2.parent
        
        
node1=Node(1,None)
node2=Node(2,node1)
node3=Node(3,node1)
node4=Node(4,node2)
        
print(lca(node4,node3))
print("Time Complexity: Suppose, the highest depth of any node in tree is n. \
Then time complexity is O(2n) in worst case. Because, first we store all n parents of node1, \
which takes n unit. Then, we iterate over parents of node2 and lookup among parents of node1 until the ica is found. \
In worst case, it takes n iteration. set() in python lookup time is O(1) in average. So, in total O(n+n*O(1))= O(2n) or O(n)")

print("\nMemory Complexity : Suppose, the highest depth of any node in tree is n. \
Them memory complexity is O(n) worst case. Because, we only need to store parents of any single node. \
Which takes n unit of memory.")