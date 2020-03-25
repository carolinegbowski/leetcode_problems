"""
67. Add Binary
Easy

1476

254

Add to List

Share
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2: 

Input: a = "1010", b = "1011"
Output: "10101"
"""

# first attempt
# def addBinary(a,b):
#     num1 = self.binaryToDecimal(a)
#         num2 = self.binaryToDecimal(b)
#         decimal_sum = str(num1 + num2)
#         return decimal_sum
#         # binary_sum = self.decimalToBinary(decimal_sum)
        
# def binaryToDecimal(num):
#     exponent = 0
#     total = 0
#     for char in num[::-1]:
#         total += (int(char) * (2**exponent))
#         exponent += 1
#     return total

# def decimalToBinary(num):

# second attempt

def addBinary(a,b):
    answer = "{0:b}".format(int(a, 2) + int(b, 2))
    return answer

print(addBinary("11", "1"))
print(addBinary("1010", "1011"))
