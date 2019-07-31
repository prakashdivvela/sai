n,p,q,r=list(map(int,input().split()))
a=list(map(int,input().split()))
b=[]
for i in range(n):
  for j in range(n):
    for k in range(n):
      if(i<=j<=k):
        c=(p*a[i])+(q*a[j])+(r*a[k])
        b.append(c)
print(max(b))
