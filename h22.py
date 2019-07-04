p=int(input(""))
q=list(map(int,input().split()))
q.sort(reverse=True)
j=0
for i in range(len(q)):
  j=(j*10)+q[i]
print(j)
