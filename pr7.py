p,q=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
  for j in range(len(l)):
    if l[i]+l[j]==q:
      c+=1
if(c>0):
  print("yes")
else:
  print("no")  
