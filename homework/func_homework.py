# Упражнения
def sum_of_tripples(a, b):
    return a**3 + b**3

result = sum_of_tripples(5, 6)
print(result)

numbers = [1, 2, 3, 4, 5, 6]

tripple_numbers = list(map(lambda x: x**3, numbers))
print(tripple_numbers)


more_three_numbers = list(filter(lambda x: x > 3, numbers))
print(more_three_numbers)


# Домашнее задание
def my_calc_function(a, b):
    return (a + b)**2 - (a**2 + b**2)

result = my_calc_function(5, 8)
print(result)


numbers = [10, 20, 30, 40, 50]
double_numbers = list(map(lambda x: x**2, numbers))
print(double_numbers)


numbers = [5, 10, 15, 20, 25]
divided_numbers = list(filter(lambda x: x % 5 == 0, numbers))
print(divided_numbers)
