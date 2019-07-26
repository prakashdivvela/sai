j=int(input())
m=list(map(int,input().split()))
l=[]
n=[]
b=[]
e=0
o=1
while(e<100000):
  l.append(e)
  e=e+2
while(o<100000):
  n.append(o)
  o=o+2
for i in range(j):
  if((m[i] in l)and (i in n)):
    b.append(m[i])
  elif((m[i] in n)and(i in l)):
    b.append(m[i])
print(" ".join(map(str,b)))
