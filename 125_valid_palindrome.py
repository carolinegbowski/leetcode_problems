"""
125. Valid Palindrome
Easy

935

2550

Add to List

Share
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    s = ''.join([x for x in s if x.isalnum()])
    return s == s[::-1]
