"""
202. Happy Number
Easy

1427

325

Add to List

Share
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

def isHappy(n):
    digits = list(str(n))
    sum_squares = 0
    already_done = set()
    
    while True:
        if sum_squares in already_done: 
            return False
        else: 
            already_done.add(sum_squares)
        
        sum_squares = 0
        for i in digits: 
            sum_squares += (int(i) * int(i))
        if sum_squares == 1:
            return True
        else: 
            digits = list(str(sum_squares))

print(isHappy(19))
print(isHappy(20))