num = int(input("Enter a number: "))
original = num
reverse = 0
temp = num
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10
if original == reverse:
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")
