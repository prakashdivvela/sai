class stack:
  def __init__(self,size=0):
    self.size=size
    self.list1=[]
  def add(self,data):
    if len(self.list1)>=self.size:
      print("stack is full")
      return
    self.list1.append(data)
  def remove(self):
    if len(self.list1)==0:
      print("stackl is empty")
      return
    data=self.list1.pop()
    return data
  def printstack(self):
    for ele in self.list1:
      print(ele)
obj=stack(5)
obj.add([10,100,200])
obj.add(10)
obj.add(10)
obj.add(10)
obj.add(10)
obj.add(10)
obj.remove()
obj.remove()
obj.printstack()
