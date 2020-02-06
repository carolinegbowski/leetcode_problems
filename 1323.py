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