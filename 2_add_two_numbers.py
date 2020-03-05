"""
2. Add Two Numbers
Medium

7188

1858

Add to List

Share
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        num1 = self.llToNum(l1, 1)
        num2 = self.llToNum(l2, 1)
        total = num1 + num2
        digits = [int(i) for i in str(total)]
        answer = ListNode(digits[0])
        pointer = answer
        for i in digits[1:]:
            mynode = ListNode(i)
            mynode.next = pointer
            pointer = mynode
        return pointer
            
    def llToNum(self, ll, multiplier):
        if not ll: 
            return 0
        else: 
            return ll.val * multiplier + self.llToNum(ll.next, multiplier*10)
        
        