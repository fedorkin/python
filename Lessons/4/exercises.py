#1
from sys import argv

script_name, time_worked, cost_per_hour, prize = argv

def calculate_salary(time_worked, cost_per_hour, prize):
    return (time_worked * cost_per_hour) + prize

print(calculate_salary(float(time_worked), float(cost_per_hour), float(prize)))

#2

numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [value for i, value in enumerate(numbers) if i > 0 and value > numbers[i-1]]
print(result)

#3
print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])

#4
numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_numbers = [i for i in numbers if numbers.count(i) == 1]
print (unique_numbers)

#5
from functools import reduce
numbers = (i for i in range(100, 1001, 2))

print(reduce(lambda x, y: x * y, numbers))

#6
from itertools import count, cycle

def next_number(start, end):
    for n in count(start):
        if n <= end:
            yield n
        else:
            break
    
print(list(next_number(1, 10)))

def repeat_list(numbers, repeat_count):
    i = 0
    for n in cycle(numbers):
        if i / len(numbers) < repeat_count:
            i +=1
            yield n
        else:
            break
print(list(repeat_list([1, 2 ,3], 2)))

#7
def fact(n):
    i = 1
    r = 1
    while i <= n:
        r *= i
        i += 1
        yield r

        
print(list(fact(4)))


    
    


