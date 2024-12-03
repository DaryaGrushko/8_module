#Сложные моменты и исключения в стеке вызовов функции
#Задача "План перехват"

def personal_sum(numbers):
    #print('Зашли в функцию personal_sum', '///  numbers=', numbers, '///   type(numbers)=', type(numbers))
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
            #print ('i = ', i, 'result = ', result)
        except TypeError as exp:
            print(f'Некорректный тип данных для подсчета данных - {i}')
            incorrect_data+=1
    #print ('result=',  result, '//  incorrect_data=', incorrect_data)
    return (result,  incorrect_data)

def calculate_average(numbers):
    #print('Зашли в функцию calculate_average', '///  numbers=', numbers )
    try:
        sum=personal_sum(numbers)
        #print ('sum = ', sum, '-[0]:', sum[0], '-[1]:', sum[1])
        arithmetic_mean = sum[0]/(len(numbers)-sum[1])
        #print ('arithmetic_mean = ', arithmetic_mean)
        return arithmetic_mean
    except (TypeError, UnboundLocalError) :
        print ('В numbers записан некорректный тип данных')
        return None
    except ZeroDivisionError as exp2:
        return 0

print ('1-------------------')
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print ('2-------------------')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print ('3-------------------')
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print ('4-------------------')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
