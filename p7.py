f=list(input())
i=0
while(i<len(f)):
  tem=f[i]
  f[i]=f[i+1]
  f[i+1]=tem
  i+=2
print("".join(f))
