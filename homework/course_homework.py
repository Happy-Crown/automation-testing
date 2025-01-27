def catch_even_numbers(numbers):
    return [x for x in numbers if x%2==0]

numbers = [1, 3, 6, 8, 9, 10]
result = catch_even_numbers(numbers)
print(result)


class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(f"Кноига: {self.title}, автор: {self.author}")

new_book = Book("В мире чудес", "Сэмуэль Джексон")
print(new_book.author, new_book.title)
new_book.info()


import os
import csv
import json

if not os.path.exists('my_csv_file.csv'):
    print("Файл не найден")
else:
    with open('my_csv_file.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]

    with open('uotput.json', 'w') as json_file:
        json.dump(data, json_file)

    print("Данные успешно записаны")
