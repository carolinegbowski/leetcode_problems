"""
3. Longest Substring Without Repeating Characters
Medium

7926

475

Add to List

Share
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring."""


def lengthOfLongestSubstring(s):
    output = []
    max_length = 0
    length = 0
    for i in range(len(s)):
        if s[i] in output: 
            if length > max_length:
                max_length = length
            index = output.index(s[i])
            output.append(s[i])
            output = output[index+1:]
            length = len(output)
        else: 
            length += 1
            output.append(s[i])
    return max(len(output), max_length)

print(lengthOfLongestSubstring("abcabcbb"))