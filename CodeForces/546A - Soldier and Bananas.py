a,b,c = map(int,input().split())
total = a*c*(c+1)//2
print (max(0,total-b))