#1
def div(x, y):
    return x / y

x = float(input("Введите x: "))
y = float(input("Введите y: "))


try:
    result = div(x, y)
    print(f"x / y = {result}")
except ZeroDivisionError:
    print("На ноль делить нельзя")

#2
def user_info(firstName, lastName, yearOfBirth, city, email, phone):
    print(f"FirstName: {firstName}, LastName: {lastName}, YearOfBirth: {yearOfBirth}, City: {city}, Email: {email}, Phone: {phone}")

user_info(firstName="Pavel", lastName="Fedorov", yearOfBirth=1984, city="Rybinsk", email="mymail@mail.ru", phone=79109998887766)

#3
def my_func(n1, n2, n3):
    maxNumbers = sorted([n1, n2, n3], reverse=True)[:2]
    return sum(maxNumbers)
print (my_func(3, 1, 5))

#4
def sqrt(x, degree):
    return x**degree

def manual_sqrt(x, degree):
    result = x
    for i in range(1, abs(degree)):
        result *= x
    return result if degree > 0 else 1 / result

x = float(input("Введите x: "))
y = int(input("Введите степень x: "))

print(f"{x} в степени {y} = {sqrt(x, y)}")
print(f"{x} в степени {y} = {manual_sqrt(x, y)}")

#5
print("Введите числа через пробел или 'q' если хотите выйти: ")
numberSum = 0
isContinue = True
while isContinue:
    array = input().split()
    for i in array:
        if i.isdigit():
            numberSum += int(i)
        elif i.lower() == 'q':
            isContinue = False
            break
    print(f'Сумма чисел равна {numberSum}')
    
    
#6
def capitalize_word(word):
    return word.capitalize()

print(int_func("слово"))
    
#7
def capitalize_word(word):
    return word.capitalize()

def capitalize_every_word(inStr):
    return ' '.join([capitalize_word(word) for word in inStr.split()])
print(capitalize_every_word("a sentense with several words"))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    