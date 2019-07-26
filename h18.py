n=input()
l=list(map(int,input().split()))
for i in range(0,n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      if(l[i]+l[j]==l[k]):
        print(l[i],l[j],l[k])
