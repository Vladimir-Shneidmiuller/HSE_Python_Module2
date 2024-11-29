'''
Задание 1
Напишите код на Python для решения следующей задачи.
Реализуйте функцию sum_distance(from, to), которая суммирует все числа от
значения from до величины to включительно.
Примечание. Если пользователь задаст первое число, которое окажется
больше второго, просто поменяйте их местами.
'''

from_value = int(input())
to_value = int(input())


def sum_distance(from_value, to_value):
    if from_value > to_value:
        from_value,to_value = to_value, from_value
    summ = sum(range(from_value, to_value + 1))
    return summ
  
print(sum_distance(from_value, to_value))




'''
Задание 2
Напишите код на Python для решения следующей задачи.
Реализуйте функцию trim_and_repeat(), которая принимает три параметра:
● строку;
● offset — число символов, на которое нужно обрезать строку слева;
● repetitions — сколько раз нужно повторить строку перед возвратом
получившейся строки.
Число символов для среза по умолчанию равно 0, а количество повторений —
1.
Функция должна возвращать полученную строку.
'''

def trim_and_repeat(string, offset=0, repetitions=1):
    new_string = string[offset:]
    res = new_string * repetitions

    return res
