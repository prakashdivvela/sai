from itertools import permutations
k=list(input())
p=permutations(k)
for i in list(p):
  print(*i,sep="")
