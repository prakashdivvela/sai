n=int(input())
k=list(map(int,input().split()))
z=input()
b=[]
for i in range(n):
  for j in range(i+1,n):
    s=k[i]+k[j]
    b.append(s)
a=min(b)
c=a*z
print(c)
