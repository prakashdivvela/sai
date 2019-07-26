n=int(input())
b=list(map(int,input().split()))
for i in range(n):
  for j in range(i+1,n):
      if(b[i]+b[j]==0):
        print(b[i],b[j])
