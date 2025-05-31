string = input("Enter a string: ")
words = string.split(" ")
largest = ""
for word in words:
    if len(word) > len(largest):
        largest = word
print("Largest word is:", largest)
