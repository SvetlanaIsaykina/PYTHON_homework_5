import random

# Задача 3. Задайте список случайных чисел от 1 до 10.
# Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают
# Список уникальных элементов [1, 4, 2, 3, 6, 7]

numbers = list(random.randint(1,10) for _ in range(random.randint(10,15)))
print(f'Список случайных чисел: {numbers}')

result = list(map(lambda x: numbers.count(x) > 1, numbers))

print(f'Количество повторений: {result.count(True)}')

print(f'Список уникальных значений: {set(numbers)}')
