# -*- coding: utf-8 -*-
"""
Created on Tue May 19 10:45:39 2020

@author: Akshat Jain
"""

def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j>0 and nums[j]<nums[j-1]:
            swap(nums , j , j-1)
            j = j-1
    return nums

def swap(nums , i , j):
    nums[i] , nums[j] = nums[j] , nums[i]

if __name__ == "__main__":
    a = [3,34,13,1,5,5,143,5,6]
    print(insertion_sort(a))