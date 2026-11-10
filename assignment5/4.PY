def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


def main():
    my_list = [3, 8, 12, 5, 20]
    print("Danh sách:", my_list)
    print("Tổng:", sum_list(my_list))


main()