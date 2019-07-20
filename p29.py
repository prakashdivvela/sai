p=int(input())
q=[]
for i in range(p):
    s=list(map(int,input().split()))
    q+=s
q.sort()
print(*q)
