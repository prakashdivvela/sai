n,k=map(int,input().split())
s=list(map(int,input().split()))
b=[]
for i in range(n):
  b.append(s[i])
b.sort(reverse=True)
print(b[k-1])
