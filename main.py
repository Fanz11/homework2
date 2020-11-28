# первое
number1 = [1, 2, 3]                                 #числа
number2 = [i * 2 for i in number1]                  #умножение на 2
print(number2)                                      #ответ


# второе
number1 = [1, 2, 3]                                #числа
number2 = [i ** 2 for i in number1]                #возведение в вторую степень
print(number2)                                     #ответ

#трертье
list = 'Hello world'
if " " in list:                                    #если есть пробел
    list = list.upper()                            #перевод в верхний регистр
    print(list)                                    #ответ
else:                                              #если нет пробела
    list = list.lower()                            #то переводиться в нижний регистр
    print(list)                                    #ответ


#четвертое
for i in range(1900, 2021):           # диапозон годов
    print(i)                          # вывод
