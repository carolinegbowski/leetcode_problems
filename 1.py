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
        index_1 = nums.index(num)
        for each_remaining_num in nums[(index_1+1):]:
            index_2 = nums.index(each_remaining_num)
            if num + each_remaining_num == target:
                index_list.append(index_1)
                index_list.append(index_2)
                return index_list

# does not work when both nubmers are the same, but at different indicies
# need to modify here