from rental import Vehicle, Renter, ElectricCar, Motorbike


# Vehicle and renter
car = Vehicle("Toyota", "Camry", "ABC-123")
renter = Renter("John", 12345)

print(car)
print(renter.rented)

car.rent()
print(car)

car.return_vehicle()
print(car)


# Invalid renter values
try:
    Renter("", 12345)
except ValueError as e:
    print(e)

try:
    Renter("Alice", 0)
except ValueError as e:
    print(e)

try:
    Renter("Bob", -1)
except ValueError as e:
    print(e)


# Invalid values when changed later
renter.name = "Jack"
renter.license_no = 999

try:
    renter.name = ""
except ValueError as e:
    print(e)

try:
    renter.license_no = 0
except ValueError as e:
    print(e)

try:
    renter.license_no = -5
except ValueError as e:
    print(e)


# Inheritance
electric = ElectricCar("Tesla", "Model 3", "EV-456", 75)
bike = Motorbike("Honda", "CBR500", "MB-789", 500)

print(isinstance(electric, Vehicle))
print(isinstance(bike, Vehicle))

electric.rent()
print(electric)
electric.return_vehicle()

bike.rent()
print(bike)
bike.return_vehicle()


# Polymorphism
vehicles = [car, electric, bike]

for vehicle in vehicles:
    print(vehicle)