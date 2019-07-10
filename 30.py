h1,m1=map(int,input().split())
h2,m2=map(int,input().split())
if h1<h2:
  h=h2-h1
else:
  h=h1-h2
if m1<m2:
  m=m2-m1
else:
  m=m1-m2
print(h,m)
