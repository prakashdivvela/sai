p=int(input())
s=list(map(int,input().split()))
x=s[0:p:2]
y=s[1:p:2]
if sum(x)>=sum(y):
  print(sum(x))
else:
  print(sum(y))
