numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
k, C = input().split()
k, C = int(k), int(C)
numbers.append(0)  
for i in range(len(numbers) - 1, k, -1):
    numbers[i] = numbers[i - 1]
numbers[k] = C

print(*numbers)
