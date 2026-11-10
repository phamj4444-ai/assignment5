numbers = []

while True:
    s = input("Nhập một số (Enter để thoát): ")
    if s == "":
        break
    numbers.append(float(s))

numbers.sort(reverse=True)
print("Năm số lớn nhất:")
for n in numbers[:5]:
    print(n)