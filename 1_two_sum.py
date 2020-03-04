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
        ## for each num in nums, find the remainder of target - num, see if it's even in the list
        remainder = target - num
        if remainder in nums:
            # find index of first val, append it to output (so we know it's already been used)
            index1 = nums.index(num)
            index_list.append(index1)
            index2 = nums.index(remainder)
            #make sure index2 isnt same as index1 (make sure we didnt already use that element)
            if index2 not in index_list:
                #if not, we're done
                index_list.append(index2)
                return index_list
            else:
                #if so, we check how many occurrances there are of said remainder
                occurrence = [i for i, n in enumerate(nums) if n == remainder]
                #if multiple, take the second occurrance
                if len(occurrence) > 1:
                    index2 = occurrence[1]
                    index_list.append(index2)
                    return index_list
                #if only one, we've used the same element twice and need to start over
                #We clear our index list and let our program check the next num
                else: 
                    index_list = []

twoSum([2,7,11,15], 9)