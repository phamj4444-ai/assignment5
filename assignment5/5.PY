def remove_odd(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result


def main():
    original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    reduced = remove_odd(original)
    print("Danh sách ban đầu:", original)
    print("Danh sách sau khi loại số lẻ:", reduced)


main()