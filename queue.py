class queue:
  def __init__(self,size=0):
    self.size=size
    self.list1=[]
  def add(self,data):
    if len(self.list1)>=self.size:
      print("queue is full")
      return
    self.list1.append(data)
  def remove(self):
    if len(self.list1)<=0:
      print("queue is empty")
      return
    data=self.list1.pop(0)
    return data
  def printqueue(self):
    for ele in self.list1:
      print(ele)
obj=queue(5)
obj.add([10,100,200])
obj.add(10)
obj.add(10)
obj.add(10)
obj.add(10)
obj.add(10)
print(obj.remove())
obj.printqueue()
