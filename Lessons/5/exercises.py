#1
import os

inStr = input("Введите строку: ")
with open(os.path.join(os.getcwd(), "1.txt"), "w") as file:
    while inStr != "":
        file.write(inStr + '\n')
    
        inStr = input("Введите строку: ")
        
#2
import os

lineCount = 0
with open(os.path.join(os.getcwd(), "2.txt"), "r") as file:
    while True:
        line = file.readline()
        if not line:
            break;
        lineCount += 1
        wordCount = len(line.split())
        print(f'Line {lineCount} words {wordCount}')


#3
import os
employeeCount = 0
commonSalary = 0.0
with open(os.path.join(os.getcwd(), "3.txt"), "r") as file:
    while True:
        line = file.readline()
        if not line:
            break;
        employeeCount += 1
        splitedLine = line.split()
        lastName = splitedLine[0]
        salary = float(splitedLine[1])
        if salary < 20000:
            print(f'LastName {lastName} salary {salary:.2f}')
        commonSalary += salary
print(f'Avg salary {commonSalary / employeeCount:.2f}')


#4
import os
numberLocalization = {"One":"Один", "Two":"Два", "Three":"Три", "Four":"Четыре"}
with open(os.path.join(os.getcwd(), "4.txt")) as readableFile:
    with open(os.path.join(os.getcwd(), "4_write.txt"), "w") as writableFile:
        while True:
            line = readableFile.readline()
            if not line:
                break
            
            for key, value in numberLocalization.items():    
                line = line.replace(key, value)
            writableFile.write(line)
      
#5
import os
with open(os.path.join(os.getcwd(), "5.txt"), "w") as writableFile:
    numbers = [23, 45, 8, 2, 34, 9]
    numbersLine = ' '.join([str(n) for n in numbers])
    writableFile.write(numbersLine)
with open(os.path.join(os.getcwd(), "5.txt"), "r") as readableFile:
    numbersLine = readableFile.readline()
    numbers = map(int, numbersLine.split())
    print(sum(numbers))

#6
import os
import re
lessons = {}
with open(os.path.join(os.getcwd(), "6.txt"), "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        lessonName = line.split(':')[0]
        lessonDurations = [int(d) for d in re.findall(r'\d+', line)]
        lessons[lessonName] = sum(lessonDurations)
print(lessons)

#7
import os
import statistics
firms = {}
profits = []
with open(os.path.join(os.getcwd(), "7.txt"), "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        splitedLine = line.split()
        firmName = splitedLine[0]
        income = int(splitedLine[2])
        expenses = int(splitedLine[3])
        profit = income - expenses
        firms[firmName] = profit
        if profit > 0:
            profits.append(profit)
summary = [firms, {"average_profit":statistics.mean(profits)}]
print(summary)

        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    