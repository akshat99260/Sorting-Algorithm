# -*- coding: utf-8 -*-
"""
Created on Tue May 19 10:37:05 2020

@author: Akshat Jain
"""

def selection_sort(nums):
    for i in range(len(nums)):
        index = i
        for j in range(i+1 , len(nums),1):
            if(nums[j]<nums[index]):
                index = j
        if(index != i):
            swap(nums,index , i)
    return nums
    
    
def swap(nums , i , j):
    nums[i] , nums[j] = nums[j] , nums[i]

if __name__ == "__main__":
    
    nums = [9,7,5,4,7,5,6,8,6,0]
    print(selection_sort(nums))