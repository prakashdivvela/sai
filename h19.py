n=int(input())
a=list(map(int,input().split()))
for i in range(n):
  for j in range(i+1,n):
      if(a[i]+a[j]==0):
        print(a[i],a[j])
