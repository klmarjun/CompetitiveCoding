n = int(input())
res = 0
denominations = [100,20,10,5,1]

for i in denominations:
    res+=n//i
    n%=i
print(res)