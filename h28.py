n=list(input())
b=[]
for i in range(len(n)):
    if n[i] not in b:
        b.append(n[i])
print("".join(map(str,b)))
