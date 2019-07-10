h1,m1=map(int,input().split())
h2,m2=map(int,input().split())
h3,m3=map(int,input().split())
if h1==h2==h3 or m1==m2==m3 or h1==m1 or h2==m2 or h3==m3:
  print("yes")
else:
  print("no") 
