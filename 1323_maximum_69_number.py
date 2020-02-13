"""
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

 

Example 1:

Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666. 
The maximum number is 9969.
Example 2:

Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
Example 3:

Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.
 

Constraints:

1 <= num <= 10^4
num's digits are 6 or 9.
"""


def maximum69Number (num):
    original_number = []
    string_num = str(num)
    
    for i in range(len(string_num)):
        original_number.append(string_num[i])
    
    new_numbers_list = []
    new_numbers_list.append(num)

    for i in range(len(string_num)):

        modified_number = []
        for num in original_number: 
            modified_number.append(num)

        if original_number[i] == "6":
            modified_number[i] = "9"
            
        if original_number[i] == "9":
            modified_number[i] = "6"
            
        final_number = "".join(modified_number)
        new_numbers_list.append(int(final_number))

    return max(new_numbers_list)

print(maximum69Number(9669))
print(maximum69Number(9999))