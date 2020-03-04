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
    # create an empty stack
    saved_opens = []
    # account for base cases
    # if the string is empty, automatic true
    if s == "":
        return True
    # if first character is not an open, automatic false 
    if s[0] not in opens:
        return False
    #iterate through string
    for char in s:
        try:
            # append opens to stack 
            if char in opens: 
                saved_opens.append(char)
            # if closed, pop off top of stack. If not matching, return False
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
        # if we get an index error while popping, not a match. return false
        except IndexError:
            return False
    # if we pop everything off and list is empty, we have valid parenthesis
    if saved_opens == []:
        return True