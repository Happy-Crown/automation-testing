
class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def __str__(self):
         return f"'{self.model}' by '{self.brand}' with {self.mileage}km mileage"

    def drive(self, distance):
        self.mileage += distance
        return self.mileage
    
    
my_car = Car("Lada", "Vesta", 2011, 20000)
print(my_car)

print(my_car.mileage)
my_car.drive(100)
print(my_car.mileage)