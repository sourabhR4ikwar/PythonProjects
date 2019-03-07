n = int(input())
arr = map(int, input().split())

numbers = list(set(arr))
maximum = numbers[0]
second_maximum = 0
for i in numbers:
    if i > maximum:
        second_maximum = maximum
        maximum = i
    elif i > second_maximum:
        second_maximum = i


print(second_maximum)
