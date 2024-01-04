n = int(input())  
x_levels = set(map(int, input().split()[1:]))  
y_levels = set(map(int, input().split()[1:]))  
 
if set(range(1, n + 1)) <= x_levels.union(y_levels):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")