n,k=map(int,input().split())
m=[]
for i in range(n):
  s=set(map(int,input().split()))
  m.append(s)
print(*s.intersection(*m))
