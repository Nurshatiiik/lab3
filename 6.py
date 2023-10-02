numbers = list(map(int, input().split()))
if len(numbers) == 0:
    print(" ")
else:
    max_value = max(numbers)
    index_of_max = numbers.index(max_value)
    print(max_value)
    print(index_of_max)