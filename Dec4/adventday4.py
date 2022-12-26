#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 11:43:12 2022

@author: aidencloud
"""

user_file = 'input.txt'

def groupList(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
        
def range_subset(range1, range2):
    if not range1:
        return True
    if not range2:
        return False
    # if len(range1) > 1 and range1.step % range2.step:
    #     return False
    return range1.start in range2 and range1[-1] in range2

def paircleaning(user_file):
    
    file = open(user_file)
    data_list = file.read().splitlines()
    init_list = []
    split_list = []
    int_list = []
    count = 0
    repeatcount = 0
    
    for i in data_list:
        init_list.append(i.split(','))
    
    for i in init_list:
        for j in i:
            split_list.append(j.split('-'))
    
    for i in split_list:
        newi = list(map(int, i))
        int_list.append(newi)
        
    grouped_list = list(groupList(int_list, 2))
        
    for i in grouped_list:
        if set((range(i[0][0],i[0][1]))).issubset(range(i[1][0],i[1][1])):
            count += 1
        elif set((range(i[1][0],i[1][1]))).issubset(range(i[0][0],i[0][1])):
            count += 1
        # if range_subset(range(i[0][0],i[0][1]), range(i[1][0],i[1][1])):
        #     count += 1
        # elif range_subset(range(i[1][0],i[1][1]), range(i[0][0],i[0][1])):
        #     count += 1
        # elif i[0] == i[1]:
        #     repeatcount += 1
        #     print(repeatcount)
            
    finalcount = count - repeatcount
        
    
    return finalcount

    
print(paircleaning(user_file))

