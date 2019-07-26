n=int(input())
c=list(map(int,input().split()))
for i in range(n):
  for j in range(i+1,n):
      if(c[i]+c[j]==0):
        print(c[i],c[j])
