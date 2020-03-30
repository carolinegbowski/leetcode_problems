"""
88. Merge Sorted Array
Easy

1683

3586

Add to List

Share
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

"""



# def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#     """
#     Do not return anything, modify nums1 in-place instead.
#     """
#     i1 = 0
#     i2 = 0
#     if nums2 == []:
#         return nums1
#     for i in range(n):
#         nums1.pop()
#     if nums1 == []:
#         nums1 += nums2[i2:]
#         return nums1
    
#     while nums2[i2] <= nums1[m-1]:
#         if nums2[i2] < nums1[i1]:
#             nums1.insert(i1-1, nums2[i2])
#             i2 += 1
#         else: 
#             i1 +=1
#     if nums2[i2:]:
#         nums1 += nums2[i2:]
        
"""
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

Failed case....
[2,0]
1
[1]
1
"""
    
    # idx = 0
    # for i in range(n):
    #     nums1.pop()
    # for num in nums2:
    #     pointer = nums1[idx]
    #     while num >= pointer:
    #         pointer = nums1[idx]
    #         idx +=1
    #     if num < pointer:
    #         if idx == 0:
    #             zero = nums1.pop()
    #             nums1.insert(0, zero)
    #             nums1[0] = num
    #         else: 
    #             zero = nums1.pop()
    #             nums1.insert(idx-1, zero)
    #             nums1[idx-1] = num
    #     else: 
    #         idx += 1
        

def merge(nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        nums1[:] = sorted(nums1[:m] + nums2)

