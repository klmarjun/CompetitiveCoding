n = int(input())
lst=[]
while(n>0):
    n-=1
    k = input()
    L = ""
    
    if(len(k)<=10):
        lst.append(k)
        
    else:
        L+=k[0]
        L+=str(len(k)-2)
        L+=k[len(k)-1]
        lst.append(L)
        
        

for i  in lst:
    print(i)