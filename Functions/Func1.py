def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))
print(f"Prime numbers between {start} and {end} are:")
for number in range(start, end + 1):
    if is_prime(number):
        print(number, end=' ')
