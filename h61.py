l,n=input().split()
l=str(l)
n=int(n)
for i in range(0,len(l)):
  if len(l[i:i+n])==n:
    print(l[i:i+n],end=" ")
