income = int(input("Введите выручку фирмы: "))
expense = int(input("Введите издержки фирмы: "))
profit = income - expense
if profit > 0:
    print("Фирма прибыльная")
elif profit < 0:
    print("Фирма убыточна")
else:
    print("Фирма работает в ноль")
