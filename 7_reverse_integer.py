"""


7. Reverse Integer
Easy

2939

4628

Add to List

Share
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


"""



def reverse(x):
    x = str(x)
    new_string = ""
    if x[0] == "-":
        for i in str(x[1:]): 
            new_string = i + new_string
        output = 0 - int(new_string)
        if output < -2147483648: 
            return 0
        else: 
            return output 
    else: 
        for i in str(x): 
            new_string = i + new_string
            output = int(new_string)
        if output > 2147483648: 
            return 0
        else: 
            return output

print(reverse(-123))
print(reverse(349))