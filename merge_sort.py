# -*- coding: utf-8 -*-
"""
Created on Wed May 20 09:57:45 2020

@author: Akshat Jain
"""

def merge_sort(nums):
    if(len(nums)==1):
        return
    middleIndex = len(nums)//2
    left_half = nums[:middleIndex]
    right_half = nums[middleIndex:]
    merge_sort(left_half)
    merge_sort(right_half)
    
    i = 0 
    j = 0
    k = 0
    
    while(i<len(left_half) and j < len(right_half)):
        if(left_half[i]<right_half[j]):
            nums[k] = left_half[i]
            i = i+1
        else:
            nums[k] = right_half[j]
            j = j+1
        k = k+1
        
    while(i<len(left_half)):
        nums[k] = left_half[i]
        k = k+1
        i = i+1
    
    while(j<len(right_half)):
        nums[k] = right_half[j]
        k = k+1
        j = j+1
    
if __name__ == "__main__":
    a = [-1,-5,-9,6,4,10,4,3,1]
    merge_sort(a)
    print(a)