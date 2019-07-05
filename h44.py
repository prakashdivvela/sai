p=int(input())
q=list(map(int,input().split()))[:p]
for i in range(p):
  if q.count(q[i])==1:
    print(q[i])
