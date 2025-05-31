start_no = int(input("Enter the start of the interval: "))
end_no = int(input("Enter the end of the interval: "))
print(f"Prime numbers between are:")
for num in range(start_no, end_no + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=' ')
