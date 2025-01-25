from functools import reduce

numbers = list(range(1, 11))
print(numbers)

squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)

more_20_numbers = list(filter(lambda x: x > 20, squared_numbers))
print(more_20_numbers)

sum_numnbers = reduce(lambda x, y: x + y, more_20_numbers)
print(sum_numnbers)
