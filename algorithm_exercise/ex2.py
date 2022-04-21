#!/usr/bin/env python
# coding: utf-8

# In[17]:


import io
import math

def find_maximum_subarray(A, low, high):
    if ( high == low ):
        return low, high, A[low]
    else:
        mid = math.floor((low + high)/2)
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(A, mid+1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)

        if (left_sum >= right_sum and left_sum >= cross_sum):
            return left_low, left_high, left_sum
        elif (right_sum >= left_sum and right_sum >= cross_sum):
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

def find_max_crossing_subarray(A, low, mid, high):
    max_left, max_right = -1, -1
    # 左半部subarray
    left_sum = float("-Inf")
    sum = 0
    for i in range(mid, low - 1, -1):
        sum += A[i]
        if ( sum > left_sum ) :
            left_sum = sum 
            max_left = i
    
    # 右半部subarray
    right_sum = float("-Inf")
    sum = 0 
    for j in range(mid+1, high+1):
        sum += A[j]
        if ( sum > right_sum ):
            right_sum = sum
            max_right = j
            
    return max_left, max_right, left_sum + right_sum

f = open('testfile_ex2.txt', 'r')
buf = io.StringIO()
mylist2 = []

with open('testfile_ex2.txt') as f:
    mylist = f.read().splitlines()
for x in mylist:
    str = x.replace("\n", "")
    if (str != ""):
        mylist2.append(x.replace("\n", ""))
        
n = 0
idx = -1
for y in mylist2:
    if ( n + 1 < len(mylist2) ):
        num = int(mylist2[n])
        print(num)
        if ( num == 0 ):
            continue
        
        tmp = mylist2[n+1].split(' ')
        data = []
        list = []
        for i in tmp:
            list.append(int(i))
            
        if ( num == 0 ):
            print('zero')
        elif( num != len(list)):
            ("")
        else:
            data.append(list)
            idx = len(data) - 1 
        
            tmp_low, tmp_high, tmp_sum = find_maximum_subarray(data[idx], 0, len(data[idx]) - 1) 
            print("Maximum: ", tmp_low+1, tmp_high+1, tmp_sum )
        
        n = n + 2
        list.clear()
    elif ( n < len(mylist2) ):
        num = int(mylist2[n])
        if ( num == 0 ):
            n = n + 2
    

