num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    smaller = num2
else:
    smaller = num1
for x in range(1, smaller + 1):
    if (num1 % x == 0) and (num2 % x == 0):
        gcd = x
print("The gcd of", num1, "and", num2, "is:", gcd)
