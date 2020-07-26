# -*- coding: utf-8 -*-
"""
Created on Tue May 19 12:04:38 2020

@author: Akshat Jain
"""

def quick_sort(nums , low , high):
    if low>=high:
        return
    pivot_index = partition(nums , low , high)
    quick_sort(nums , low , pivot_index-1)
    quick_sort(nums , pivot_index+1 , high)
    
def partition(nums ,low,high):
    
    pivot_index = (low+high)//2
    swap(nums , pivot_index , high)
    i = low
    for j in range(low , high , 1):
        if(nums[j]<=nums[high]):
            swap(nums,j,i)
            i= i+1
    
    swap(nums,high , i)
    return i  
def swap(nums ,i,j):
    nums[i] , nums[j] = nums[j] , nums[i]

if __name__=="__main__":
    a = [9,4,0,7,1,4,0,8,5,0]
    quick_sort(a,0,len(a)-1)
    print(a)