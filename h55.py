n,m=map(int,input().split())
l=list(map(int,input().split()))
for i in range(m):
  l=l[1:]+l[:1]
print(*l,end=" ")
