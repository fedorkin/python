#1
l = ["a", 2, 3.14, "4"]
for x in l:
    print(f'{x} is type:{type(x)}')
    
#2
inStr = input("Введите значения через запятую: ")
array = inStr.split(',')
output = []
for i, v in enumerate(array):
    if i % 2:
        value = array[i - 1]
        array[i - 1] = array[i]
        array[i] = value
print(array)

#3
months = [x for x in range(1, 13)]
seasons = ["зима" for _ in range(2)] + ["весна" for _ in range(3)] + ["лето" for _ in range(3)] + ["осень" for _ in range(3)] + ["зима"] 
calendar = dict(zip(months, seasons))
inMonth = int(input("Введите номер месяца от 1 до 12: "))
print(f"Это {calendar[inMonth]}")

#4
inStr = input("Введите несколько слов разделенные пробелами: ")
words = inStr.split()
for i, word in enumerate(words):
    print(f'{i} - {word[:10]}')

#5
numbers = []
while (True):
    inNum = int(input("Введите число: "))

    
    for i, currentNum in enumerate(numbers):
        if inNum > currentNum:
            numbers.insert(i, inNum)
            break
        elif i == len(numbers) - 1:
            numbers.append(inNum)
            break

        
    if len(numbers) == 0:
        numbers.append(inNum)
        
    print(numbers)
    
#6
store = []
while True:
    productName = input("Название товара: ")
    productPrice = int(input("Цена товара: "))
    productCount = int(input("Количество: "))
    productUnit = input("Единицы измерения: ")
    prod = {"название":productName, "цена":productPrice, "количество":productCount, "ед":productUnit}
    index = len(store) + 1
    store.append((index, prod))
    
    print(store)
    
    summary = {"название":[], "цена":[], "количество":[], "ед":[]}
    
    for s in store:
        summary = {key: list(set(value + [s[1][key]])) for key, value in summary.items()}
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    