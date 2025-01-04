n = int(input())
X =0
for count in range(0,n):
    user_input = input()
    if user_input == "++X" or user_input == "X++":
        X +=1
    else:
        X -= 1
print(X)