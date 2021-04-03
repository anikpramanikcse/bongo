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
        if isinstance(cur,Person):
            cur=cur.__dict__
        for key in cur:    
            print(key,depth)
            if(isinstance(cur[key], dict) or isinstance(cur[key], Person)):
                queue.append(cur[key])
                queue.append(depth+1)
      

class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father



person_a = Person('User', '1', None)
person_b = Person('User', '2', person_a)


a = {'key1': 1,
     'key2': {
         'key3': 1,
         'key4': {
             'key5': 4,
             'user': person_b
                 }
              }
    }

print_depth(a)