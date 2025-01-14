k, r = map(int, input().split())
n = 1

while True:
    total_cost = n * k
    if total_cost % 10 == 0 or total_cost % 10 == r:
        print(n)
        break
    n += 1 