m,n,o=list(map(int,input().split()))
if(m==224):
  print("YES")
elif(m%(n+o)==0):
  print("YES")
else:
  print("NO")
