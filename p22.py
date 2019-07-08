a,b=map(int,input().split())
r=list(map(int,input().split()))
for i in range(b):
  s,t=map(int,input().split())
  print(sum(r[s-1:t]))
