"""
53. Maximum Subarray
Easy

6308

272

Add to List

Share
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

def maxSubArray(nums):
    if nums == []:
        return 0
    if len(nums) == 1: 
        return nums[0]
    if len(nums) == 2:
        if sum(nums) > max(nums): 
            return sum(nums)
        else:
            return max(nums)
    else: 
        max_sum = nums[0]
        tally = nums[0]
        for i in nums[1:]:
            tally += i
            if tally > max_sum:
                max_sum = tally
            if i > max_sum:
                max_sum = i
                tally = i
            if tally < 0:
                tally = 0
    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([8, -19, 5, -4, 20]))
