def tap_hop():
    numbers =[]
    
    while True:
        value= input("nhap so nguyen (hoac q to quit):")
        if value == "q":
            break
        num= int(value)
        numbers.append(num)
    print("lisst of numbers:", numbers)
    total= sum(numbers)
    print(total)
tap_hop()
