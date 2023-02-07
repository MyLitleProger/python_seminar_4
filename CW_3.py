# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
#
# *Пример:*
#
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

number_list = [1, 2, 3, 5, 1, 5, 3, 10]
print(*number_list, end=' -> ')
print(*[letter for letter in number_list if number_list.count(letter) == 1])
