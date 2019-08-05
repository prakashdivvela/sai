x,y=map(list,input().split())
c=abs(len(x)-len(y))
for i in range(len(a)):
    if len(y)==1 and y[i] in a:
        break
    if x[i]!=y[i]:
        c+=1
print(c)
