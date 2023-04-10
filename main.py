class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def __str__(self):
        return f"Vehicle type: {self.vehicle_type}"

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def __str__(self):
        return f"{super().__str__()}\nYear: {self.year}\nMake: {self.make}\nModel: {self.model}\nNumber of doors: {self.doors}\nType of roof: {self.roof}"

def main():
    vehicle_type = input("Enter the vehicle type: ")
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")

    car = Automobile(vehicle_type, year, make, model, doors, roof)

    print(car)

if __name__ == '__main__':
    main()
