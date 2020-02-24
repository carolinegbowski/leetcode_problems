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
        remainder = target - num
        if remainder in nums:
            index1 = nums.index(num)
            index_list.append(index1)
            index2 = nums.index(remainder)
            if index2 not in index_list:
                index_list.append(index2)
                return index_list
            else:
                occurrence = [i for i, n in enumerate(nums) if n == remainder]
                if len(occurrence) > 1:
                    index2 = occurrence[1]
                    index_list.append(index2)
                    return index_list
                else: 
                    index_list = []

twoSum([2,7,11,15], 9)