sai = int(input())
s=[]
for i in range(0,sai):
 inpu=input()
 s.append(inpu)
li=[]
for i in zip(*s):
 if(i.count(i[0])==len(i)):
  li.append(i[0])
 
 else:
  break
print(''.join(li))
