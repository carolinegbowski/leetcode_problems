"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

def twoSum(nums, target):
    index_list = []
    for num in nums: 
        for each_remaining_num in nums[num:]:
            if num + each_remaining_num == target:
                index_list.append(nums.index(num))
                index_list.append(nums.index(each_remaining_num))
    return index_list