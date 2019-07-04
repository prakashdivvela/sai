n1,n2=map(str,input("").split())
if(len(n1)!=len(n2)):
  print("no")
a=[n1.count(i) for i in n1]
b=[n2.count(i) for i in n2]
if(a==b):
  print("yes")
else:
  print("no")
