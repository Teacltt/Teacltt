month=int(input('Введите месяц: '))
day=int(input('Введите день: '))
if month <=2 or month == 12:
    if month==2 and day <=28:
            print('Это зима.')
    elif month <2 or month == 12 and day <=31:
            print ('Это зима.')
    else:
            print('Неверная дата')
elif month <=5 and month >=3:
    if day <=31:
            print('Это весна')
    else:
            print('Неверная дата')
elif month <=8 and month >=6:
    if day <=31:
            print('Это лето')
    else:
            print('Неверная дата')
elif month <=11 and month >=9:
    if month == 11 and day <31:
            print('Это осень')
    elif month <11 and month >=9 and day <=31:
            print('Это осень')
    else:
            print('Неверная дата')
else:
    print('Неверная дата')