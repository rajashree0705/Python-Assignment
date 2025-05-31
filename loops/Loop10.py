base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent (integer): "))
result = 1
for i in range(exponent):
    result *= base
print(f"The power of thr no. is {result}")
