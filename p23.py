p,q=map(int,input().split())
r=list(map(int,input().split()))
for i in range(q):
  s,t=map(int,input().split())
  print(min(r[s-1:t]))
