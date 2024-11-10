"""
Задание 1
Дана переменная, в которой хранится слово из латинских букв. Напишите код, который выводит на экран:
среднюю букву, если число букв в слове нечётное;
две средних буквы, если число букв чётное 

Пример работы программы:
 1. word = 'test' Результат: es
 2. word = 'testing' Результат: t
""" 

variable = str(input())
print ("Word =", variable)

if len(variable) % 2 == 0:
    index1 = len(variable)//2-1 
    index2 = index1 + 1
    for i in index1, index2:
        print(variable[i], end="")
else:
    index1 = len(variable)//2
    print(variable[index1], end="")
