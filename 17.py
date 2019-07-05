q=int(input())
s=0
a=q
while q>0:
  b=q%10
  s=s+b*b*b
  q=q//10
if a==s:
  print("yes")
else:
  print("no")
