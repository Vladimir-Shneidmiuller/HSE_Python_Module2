'''
Печатные газеты использовали свой формат дат для каждого выпуска. Для каждой
газеты из списка напишите формат указанной даты для перевода в объект datetime:
The Moscow Times - Wednesday, October 2, 2002
The Guardian - Friday, 11.10.13
Daily News - Thursday, 18 August 1977
Пример работы программы
Программа должна выводить на экран объекты типа datetime, соответствующие датам
в условии задачи/
'''

d_info = [
    ("The Moscow Times", "Wednesday, October 2, 2002", "%A, %B %d, %Y"),
    ("The Guardian", "Friday, 11.10.13", "%A, %d.%m.%y"),
    ("Daily News", "Thursday, 18 August 1977", "%A, %d %B %Y")
]

for news, d_str, d_f in d_info:
    date_obj = datetime.strptime(d_str, d_f)
    print(f"{news}: {date_obj}")
