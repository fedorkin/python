n = int(input())
ITERATION = 3
sum = 0
for i in range(1, ITERATION + 1):
    sum += int(str(n) * i)
print(sum)