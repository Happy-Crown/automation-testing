
class Car:
    def __init__(self, brand, model, year, mileage=0):
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

# Проверка увеличения пробега
print(my_car.mileage)
my_car.drive(100)
print(my_car.mileage)

# Проверка увеличения пробега несколько раз подряд
my_car.drive(10)
my_car.drive(20)
my_car.drive(50)
print(my_car.mileage)

# Создание второго экземпляра класса
fren_car = Car("Shevrale", "Niva", 2000, 5000)
print(fren_car)
print(fren_car.mileage)
fren_car.drive(200)
print(fren_car.mileage)