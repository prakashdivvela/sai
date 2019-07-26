n=int(input())
b=list(map(int,input().split()))
for i in range(0,n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      if(b[i]+b[j]==b[k]):
        print(b[i],b[j],b[k])
