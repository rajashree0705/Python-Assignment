def decimal_to_binary(number):
    binary = ""
    if number == 0:
        return "0"
    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2
    return binary


num = int(input("Enter a decimal number: "))
print("Binary number is:", decimal_to_binary(num))
