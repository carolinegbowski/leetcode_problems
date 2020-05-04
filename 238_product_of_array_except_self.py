'''
238. Product of Array Except Self
Medium

4349

379

Add to List

Share
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''


def productExceptSelf(nums):
    length = len(nums)
    l, r, output = [0]*length, [0]*length, [0]*length
    l[0] = 1
    for i in range(1, length):
        l[i] = l[i-1] * nums[i-1]
    r[length-1] = 1
    for i in reversed(range(length-1)):
        r[i] = r[i+1] * nums[i+1]
    for i in range(length):
        output[i] = l[i] * r[i]
    return output
        
        