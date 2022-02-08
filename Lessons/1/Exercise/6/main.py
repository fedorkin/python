income = float(input("Введите выручку фирмы: "))
expense = float(input("Введите издержки фирмы: "))
profit = income - expense
if profit > 0:
    print("Фирма прибыльная")

    profitability = profit / expense * 100
    print(F'Рентабельность фирмы: {round(profitability, 2)}%')

    employeesNumber = int(input("Введите количество работников: "))
    profitPerEmploy = profit / employeesNumber
    print(F'Прибыль на каждого сотрудинка состовляет: {round(profitPerEmploy, 2)}')

elif profit < 0:
    print("Фирма убыточна")
else:
    print("Фирма работает в ноль")
