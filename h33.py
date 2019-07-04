f=[]
z=int(input())
a=list(map(int,input().split()))[:z] 
for i in range(0,z):
    if (a[i]==i):
        f.append(a[i])
        f.sort()
if(len(f)>0):
    print(*f,sep=" ")
else:
    print(-1)
