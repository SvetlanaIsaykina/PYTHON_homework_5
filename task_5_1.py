import random

# Задача 1. Задайте список случайных чисел от 1 до 10,
# выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8


numbers = list(random.randint(1,10) for _ in range(random.randint(8,16)))
print(numbers)

result = filter(lambda num: num > 5, numbers)
print(list(result))