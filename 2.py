a = input().split()
a = [int(element) for element in a]

for number in a:
    if number % 2 == 0:
        print(number)
