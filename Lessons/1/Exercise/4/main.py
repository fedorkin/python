input_str = input("Введинте число: ")
i = 1
maxNum = int(input_str[0])
while i < len(input_str):
    curNum = int(input_str[i])
    if maxNum < curNum:
        maxNum = curNum
    i += 1

print(F'The max number is {maxNum}')