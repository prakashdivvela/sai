n=input()
l=list(map(int,input().split()))
a=[]
b=[]
for i in range(len(l)):
  a=l[:i+1]
  b.append(min(a))
print(*b,end=" ")
