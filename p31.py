p=int(input())
s=list(map(int,input().split()))
av=int(p/2)
x=s[av:]
y=s[::av]
if sum(x)//len(x)==sum(y)//len(y):
  print("yes")
else:
  print("no")
