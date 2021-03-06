"""
136. Single Number
Easy

3558

141

Add to List

Share
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4


"""


def singleNumber(nums):
    nums.sort()
    i = 0
    while i+1 < len(nums):
        if nums[i] == nums[i+1]:
            i += 2
        else: 
            return nums[i]
    return nums[-1]


singleNumber([4,1,2,1,2])

def singleNumberAlternativeSolution(nums):
    data = {}
    for i in nums: 
        if i in data:
            data[i] +=1
        else: 
            data[i] = 1
    for k,v in data.items():
        if v == 1: 
            return k

singleNumberAlternativeSolution([4,1,2,1,2])
