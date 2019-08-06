n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
i=0
count=0
while a[i]!=b[i]:
    a=a[1:]+a[:1]
    count=count+1
    i=i+1
print(count)
