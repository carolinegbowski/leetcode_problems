"""
283. Move Zeroes
Easy

3061

105

Add to List

Share
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""

def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    counter = 0
    for i in nums:
        if i == 0: 
            counter += 1
    while 0 in nums: 
        nums.remove(0)
    for i in range(counter):
        nums.append(0)
            

moveZeroes([0,1,0,3,12])