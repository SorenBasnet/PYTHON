#!/bin/python 


arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

"""
arr = [[11, 2,  4], 
       [4,  5,  6], 
       [10, 8, -12]]
"""

#print(f"{len(arr)}")

#print(f"{len(arr[0])}")

nrow = len(arr) 
ncol = len(arr[0]) 

for i in range(0, nrow):
    for j in range(0, ncol): 
        if j == i: 
            print(arr[i][j])

    
    for k in range(ncol, 0, -1): 
        if k == i: 
            print(f"Other diagnol : {arr[i][k-1]}")






