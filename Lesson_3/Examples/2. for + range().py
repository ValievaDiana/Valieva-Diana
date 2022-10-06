""" Урок 2 - Функция range() + цикл for"""

'''
Range() — это встроенная функция Python, которая возвращает итерируемый объект
(range object), содержащий целые числа. С помощью функция range() можно 
сгенерировать последовательность чисел с определенным шагом — далее их можно
легко перебирать с помощью цикла for.

Функцию range() можно использовать с одним или несколькими параметрами. 
В документации Python синтаксис выглядит следующим образом:

range(stop)  # с одним параметров
range(start, stop[, step])  # с несколькими параметрами
У функции 3 параметра:

start — начало последовательности [включительно] (не обязательный параметр, 
по умолчанию равен 0).
stop — задает точку остановки последовательности [значение не включено в
последовательность] (обязательный параметр).
step — шаг последовательности (не обязательный параметр, по умолчанию равен 1).
'''

# от 0 до stop (не включая значение stop)
for i in range(7):
    print(i, end=' ')  # 0 1 2 3 4 5 6

# от start до stop
for i in range(4, 11):
    print(i, end=' ')  # 4 5 6 7 8 9 10

# от start до stop с шагом step
for i in range(4, 11, 2):
    print(i, end=' ')  # 4 6 8 10

# последовательность в обратном порядке (не включая значение stop)
for i in range(10, 0, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1

'''
При работе с range() важно помнить следующее:
- Значение stop не входит в последовательность;
- Все аргументы функции должны быть целыми числами (положительными или 
отрицательными);
-При отрицательном шаге step нужно помнить, что значение start должно быть
больше значения stop;
-Значение step не должно быть равно 0, иначе Python вызовет исключение
 "ValueError".
'''

'''
Если вам нужно получить доступ к индексам списка, не очевидно как использовать 
цикл for для этой задачи. Мы можем получить доступ ко всем элементам, 
но индекс элемента остается недоступным. 

Есть способ получить доступ как к индексу элемента, так и к самому элементу.
Для этого используйте функцию range() в сочетании с функцией длины len():
'''

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21]

for i in range(len(fibonacci)):
    print(i, fibonacci[i])

# 0 0
# 1 1
# 2 1
# 3 2
# 4 3
# 5 5
# 6 8
# 7 13
# 8 21

"""
Встроенная функция enumerate() позволяет автоматически считать итерации цикла.
Ее синтаксис:

for counter, value in enumerate(some_list):  # value- итерируемый объект
    print(counter, value) # counter - порядковый номер

Функция enumerate также принимает необязательный аргумент (значение начала 
отсчета, по умолчанию 0), который делает ее еще более полезной.

"""

# Пример:
my_list = ['яблоко', 'банан', 'вишня', 'персик']

for c, value in enumerate(my_list, 1):
    print(c, value)

# 1 яблоко
# 2 банан
# 3 вишня
# 4 персик