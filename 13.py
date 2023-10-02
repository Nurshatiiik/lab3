numbers = input().split()
count_pairs = 0
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            count_pairs += 1

print(count_pairs)