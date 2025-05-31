s = input("Enter a string: ")
result = ""

for char in s:
    if char.isalpha():
        result += char

print("String with only alphabets:", result)
