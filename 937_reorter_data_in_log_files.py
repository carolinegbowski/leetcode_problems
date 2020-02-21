"""
937. Reorder Data in Log Files
Easy

427

1328

Add to List

Share
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
 

Constraints:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.
"""



def reorderLogFiles(logs):
    alpha = []
    digits = []
    final = []
    for string in logs:
        list_of_string = string.split()
        if list_of_string[1].isalpha():
            list_of_string = list_of_string[1:] + [list_of_string[0]]
            alpha.append(list_of_string)
        else:
            digits.append(" ".join(list_of_string))
    alpha.sort()
    for string in alpha:
        string = [string[-1]] + string[0:-1]
        string = " ".join(string)
        final.append(string)
    return final + digits


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(reorderLogFiles(logs))
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
print(reorderLogFiles(logs))