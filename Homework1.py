# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

num = int(input('Введите номер дня недели: '))

if 0 < num < 6:
    print('Рабочий день')
elif 5 < num < 8:
    print('Выходной день')
else:
    print('Неправильный ввод')
