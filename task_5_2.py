import random

# Задача 2. Дан список случайных чисел. Создайте список, в
# который попадают числа, описывающие возрастающую
# последовательность. Порядок элементов менять нельзя. 
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

numbers = list(random.randint(1,100) for _ in range(random.randint(25,30)))
print(numbers)

index = random.randint(0, len(numbers)-1)
rand_list = [numbers[index]]

while index < len(numbers):
    index = random.randint(index, len(numbers))
    if index != len(numbers) and numbers[index] > rand_list[-1]:
        rand_list.append(numbers[index])

print(rand_list)
