
class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def __str__(self):
         return f"'{self.model}' by '{self.brand}' with {self.mileage}km mileage"

    # Метод для увеличения пробега автомобиля
    def drive(self, distance):
        if distance < 0:
            raise ValueError("Пробег не может быть уменьшен!")
        self.mileage += distance
    
    
my_car = Car("Lada", "Vesta", 2011, 20000)
print(my_car)

print(my_car.mileage)
my_car.drive(100)
print(my_car.mileage)
