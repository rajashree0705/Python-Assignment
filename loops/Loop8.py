num = int(input("Enter a number: "))
total = 0
temp = abs(num)
while temp > 0:
    digit = temp % 10
    total += digit
    temp = temp // 10
print("The sum of digits of", num, "is", total)
