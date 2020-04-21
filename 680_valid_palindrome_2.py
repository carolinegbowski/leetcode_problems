"""

680. Valid Palindrome II
Easy

1297

93

Add to List

Share
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""

def isPalindrome(s):
        if s == s[::-1]:
            return True
        else: 
            return False

def validPalindrome(s):
    #check if original string is palindrome
    #else iterate through string
    #removing current letter, seeing if remaining string is palindrome
    if isPalindrome(s):
        return True
    p1 = 0
    p2 = -1
    while p1 <= len(s)/2:
        if s[p1] != s[p2]:
            s1 = s[:p1] + s[p1+1:]
            s2 = s[:(len(s) + p2)] + s[len(s) + p2 + 1:]
            return isPalindrome(s1) or isPalindrome(s2)
        else:
            p1 += 1
            p2 -= 1

    

