currentResultKM = firstDayKM = int(input("Сколько километров спорстмен пробежал в первый день?: "))
desiredResultKM = int(input("Желаемый результат (км): "))
dayRatio = 1.1 # 10%
dayCount = 1
while currentResultKM < desiredResultKM:
    currentResultKM *= dayRatio
    dayCount += 1

print(F"Результат будет достугнут на {dayCount} день")