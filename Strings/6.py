s = input("Enter a string: ")
reverse = ""
for char in s:
    reverse = char + reverse
if s == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
