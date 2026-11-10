#người dùng tự nhập danh sách
class list:
    def sort_list():
        numbers =[]
        while True:
            value=input("enter a number(q to quit):")
            if value == "q":
                break
            numbers.append(int(value))
        numbers.sort
        print("sorted list:",numbers)
    sort_list()