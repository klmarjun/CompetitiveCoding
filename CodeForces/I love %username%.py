n = int(input())
lst = list(map(int, input().split()))
maximum = lst[0]
minimum = lst[0]
amazing = 0

for i in lst[1:]:
    if i > maximum:
        amazing += 1
        maximum = i
    elif i < minimum:
        amazing += 1
        minimum = i

print(amazing)
