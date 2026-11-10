n = int(input("Nhập một số nguyên: "))

if n < 2:
    is_prime = False
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print(n, "là số nguyên tố")
else:
    print(n, "không phải là số nguyên tố")