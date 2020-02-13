"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

def isValid(s):
    opens = ["(", "{", "["]
    saved_opens = []
    if s == "":
        return True
    if s[0] not in opens:
        return False
    for char in s:
        try:
            if char in opens: 
                saved_opens.append(char)
            if char == ")":
                popped = saved_opens.pop()
                if popped != "(":
                    return False
            if char == "]":
                popped = saved_opens.pop()
                if popped != "[":
                    return False
            if char == "}":
                popped = saved_opens.pop()
                if popped != "{":
                    return False
        except IndexError:
            return False
    if saved_opens == []:
        return True