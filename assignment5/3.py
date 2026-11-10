cities = []

for i in range(5):
    name = input("Nhập tên thành phố thứ " + str(i + 1) + ": ")
    cities.append(name)

print("Các thành phố đã nhập:")
for city in cities:
    print(city)