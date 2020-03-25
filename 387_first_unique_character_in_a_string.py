"""
387. First Unique Character in a String
Easy

1559

101

Add to List

Share
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

from collections import Counter

def firstUniqChar(s):
    data = Counter(s)
    for i in range(len(s)):
        if data[s[i]] == 1:
            return i
    return -1

print(firstUniqChar("leetcode"))