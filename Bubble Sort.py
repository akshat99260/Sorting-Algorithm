# -*- coding: utf-8 -*-
"""
Created on Tue May 19 10:13:20 2020

@author: Akshat Jain
"""

def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(0 , len(nums)-1-i, 1):
            if(nums[j]>nums[j+1]):
                swap(nums , j , j+1)
    return nums
            
        
def swap(nums , i , j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

if __name__ == "__main__":
    
    a = ['b','c','a','u','y','w']
    print(bubble_sort(a))