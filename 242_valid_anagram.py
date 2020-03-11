"""
242. Valid Anagram
Easy

1177

129

Add to List

Share
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

def isAnagram(s,t):
    s = [i for i in s]
    t = [i for i in t]
    s.sort()
    t.sort()
    return t==s
