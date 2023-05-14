# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 11:59:10 2022

@author: Bisar
"""

import re 
regobj = re.compile('ab*c') #re.compile(pattern,flag=0)
# print(type(regobj)) #<class 're.Pattern'>
lst = ['abc','abbc','abbbbbc','acbbbbc']
for i in lst:
    st = re.match(regobj, i)
    print(str(st))

