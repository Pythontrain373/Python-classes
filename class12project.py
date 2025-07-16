def decimal_to_binary_manual(decimal_num):
    if decimal_num == 0:
        return "0"
    binary_string = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_string = str(remainder) + binary_string
        decimal_num //= 2
    return binary_string

decimal_number =int(input("What is the number: "))
binary_representation = decimal_to_binary_manual(decimal_number)
print(binary_representation)
#i copied from google next class can you please help me to understand this thank you