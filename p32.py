q=int(input())
r=list(map(int,input().split()))
x=r[0:q:2]
y=r[1:q:2]
if sum(x)>=sum(y):
  print(sum(x))
else:
  print(sum(y))
