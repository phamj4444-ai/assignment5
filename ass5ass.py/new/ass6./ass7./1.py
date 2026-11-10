class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number  
        self.max_speed = max_speed                   
        self.current_speed = 0                         
        self.travelled_distance = 0                   

if __name__ == "__main__":
    car = Car("ABC-123", 142)

    print("Biển số xe:", car.registration_number)
    print("Tốc độ tối đa:", car.max_speed, "km/h")
    print("Tốc độ hiện tại:", car.current_speed, "km/h")
    print("Quãng đường đã đi:", car.travelled_distance, "km")