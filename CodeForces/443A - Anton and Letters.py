s = input()
a = set()
 
for char in s:
    if 'a' <= char <= 'z':
        a.add(char)
 
print(len(a))