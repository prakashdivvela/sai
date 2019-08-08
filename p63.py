n=list(input())
b=[]
d=[]
for i in range(len(n)):
    if n[i] not in b :
        b.append(n[i])
    elif n[i] in b:
        break
    d.append(len(b))
print(max(d))
