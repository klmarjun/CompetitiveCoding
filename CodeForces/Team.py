x = int(input())
sum = 0
for i in range(x):
    n=3
    lst = [int(n) for n in input().split()]
    if lst[0]+lst[1]+lst[2]>=2:
        sum+=1
    else:
        sum+=0
print(sum)