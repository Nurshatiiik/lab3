x = input().split()
x = list(map(int, x))  
min_index = x.index(min(x))
max_index = x.index(max(x))
x[min_index], x[max_index] = x[max_index], x[min_index]

print(*x)