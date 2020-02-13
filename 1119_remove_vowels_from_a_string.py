"""
Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

 

Example 1:

Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:

Input: "aeiou"
Output: ""
 

Note:

S consists of lowercase English letters only.
1 <= S.length <= 1000
"""

def removeVowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    new_string = ""
    for i in s: 
        if i not in vowels:
            new_string += i
    return new_string

removeVowels("leetcodeisacommunityforcoders")

