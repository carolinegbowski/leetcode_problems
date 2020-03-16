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
    count = 0 
    i = 0
    while i+1 < len(nums):
        if nums[i] == nums[i+1]:
            i += 2
        else: 
            return nums[i]
    return nums[-1]


singleNumber([4,1,2,1,2])