a=int(input())
b=list(map(int,input().split()))
x=b[0:a:2]
y=b[1:a:2]
if sum(x)>=sum(y):
  print(sum(x))
else:
  print(sum(y))
