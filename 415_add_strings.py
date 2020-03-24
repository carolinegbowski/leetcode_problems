"""
415. Add Strings
Easy

735

218

Add to List

Share
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

def numberConverter(num):
    data = {}
    for i in range(10):
        data[str(i)] = i
    num_list = [char for char in num]
    print(num_list)
    for i in range(len(num_list)): 
        num_list[i] = data[num_list[i]]
    num_list.reverse()
    final_num = 0
    for i in range(len(num_list)):
        final_num += (num_list[i]*(10**i))
    return final_num
        

def addStrings(num1, num2):
    newNum1 = numberConverter(num1)
    newNum2 = numberConverter(num2)
    return str(newNum1 + newNum2)

print(addStrings("9", "99"))
        
        