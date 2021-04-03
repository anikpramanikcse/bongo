# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 17:24:37 2021

@author: Anik
"""

import collections

def print_depth(data):
    depth=1
    queue = collections.deque()
    queue.append(data)
    queue.append(depth)
    while queue:
        cur=queue.popleft()
        depth=queue.popleft()
        for key in cur:
            print(key," ",depth)
            if(isinstance(cur[key], dict)):
                queue.append(cur[key])
                queue.append(depth+1)
        

a = {'key1': 1,
     'key2': {
         'key3': 1,
         'key4': {
             'key5': 4
                 }
              }
    }

print_depth(a)