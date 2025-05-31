def binary_decimal(binary_str):
    decimal = 0
    length = len(binary_str)

    for i in range(length):
        digit = int(binary_str[i])
        decimal += digit * (2 ** (length - i - 1))
    return decimal


input = input("Enter a binary number: ")
print("Decimal number is:", binary_decimal(input))
