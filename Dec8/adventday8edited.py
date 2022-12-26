#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 17:21:30 2022

@author: aidencloud
"""
import numpy as np



def treetops(user_file):
    
    file = open(user_file)
    file_data = file.read().splitlines()
    lists_of_strings = [list(x) for x in file_data]
    lists_of_ints = []
    
    for i in lists_of_strings:
        int_i = list(map(int,i))
        lists_of_ints.append(int_i)
        
    init_arr = np.array(lists_of_ints)
    
    edgescount = (2 * np.shape(init_arr)[0]) + (2 * (np.shape(init_arr)[1] - 2))
    row_total = 0
    row_vis_list = []
    col_vis_list = []
    col_total = 0
    cross_total = 0
    
    for row in range(1,len(init_arr)-1):
        temp = list(init_arr[row])
        temp2 = []
        for i in range(1,len(temp)-1):
            left = temp[:i]
            right = temp[i+1:]
            if all(x < temp[i] for x in left) or all(x < temp[i] for x in right):
                row_total += 1
                temp2.append((temp[i],i))
        row_vis_list.append(temp2)
    print(row_vis_list)

    for col in range(1,np.shape(init_arr)[1]-1):
        temp = list(init_arr[:,col])
        temp2 = []
        for i in range(1,len(temp)-1):
            top = temp[:i]
            bottom = temp[(i+1):]
            if all(x < temp[i] for x in top) or all(x < temp[i] for x in bottom):
                col_total += 1
                temp2.append((temp[i],i))
        col_vis_list.append(temp2)
    #print(col_vis_list)

    for i in row_vis_list:
        for j in i:
            col = list(init_arr[:,j[1]])
            print(col)
            top = col[:j[1]]
            bottom = col[(j[1]+1):]
            print(top)
            print(bottom)
            print(j[0])
            if all(x < j[0] for x in top) or all(x < j[0] for x in bottom):
                cross_total += 1
                

    
    res = edgescount + row_total + col_total - cross_total
        
    return '''
    Trees on edges: {0}
    Trees visible from left or right: {1}
    Trees visible from top or bottom: {2}
    Trees visible from both directions: {3}
    Total trees visible: {4}
    '''.format(edgescount, row_total, col_total, cross_total, res)

print(treetops('test.txt'))