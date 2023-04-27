class Node: #to create a node
  def __init__(self,value):
    self.value = value
    self.next = None
  
class LinkList:
  def __init__(self,value): #constructor
    newNode = Node(value)
    self.head =newNode
    self.tail = newNode
    self.length = 1
 
  def append(self,value):
    newNode = Node(value)
    if self.head is None: # if linkedlist is empty
      self.head = newNode
      self.tail = newNode
        
    else:
      self.tail.next = newNode
      self.tail = newNode
    self.length += 1
    return True

  def prepend(self,value):
    newNode = Node(value)
    if self.length == 0:
      self.head = newNode
      self.tail = newNode
    else:
      newNode.next = self.head
      self.head = newNode
    self.length += 1
    return True
    
  def insert(self, index, value):
    if index <0 or index >= self.length:
      return False
    if index == 0:
      return self.prepend(value)
    if index == self.length:
      return self.append(value)
    newNode = Node(value)
    temp = self.get(index-1)
    newNode.next = temp.next
    temp.next = newNode
    self.length += 1
    return True

  def pop(self):
    if self.length == 0:
      return None
    temp = self.head
    pre = self.head
    while temp.next:
      pre = temp
      temp = temp.next
    self.tail = pre
    self.tail.next = None
    self.length -= 1
    if self.length == 0: #if only 1 node is present(length will be 0 by above code)
      self.head = None
      self.tail = None
    return temp
  
  def popFirst(self):
    if self.length == 0:
      return None
    temp = self.head
    self.head = self.head.next
    temp.next = None
    self.length -= 1
    if self.length == 0:
      self.tail = None
    return temp

  def remove(self, index):
    if index <0 or index >= self.length:
      return None
    if index == 0:
      return self.popFirst()
    if index == self.length-1:
      return self.pop()
    prev = self.get(index-1)
    temp = prev.next
    prev.next = temp.next
    temp.next = None
    self.length -=1
    return temp

  def get(self, index):
    if index < 0 or index >= self.length:
      return None
    temp = self.head
    for _ in range(index):
      temp = temp.next
    return temp

  def setValue(self, index, value):
    temp = self.get(index)
    if temp:
      temp.value = value
      return True
    return False

  def printList(self):
    temp = self.head
    while temp is not None:
      print(temp.value)
      temp = temp.next
  
  def reverse(self):
    temp = self.head
    self.head = self.tail #Updating head and tail pointer
    self.tail = temp
    current = temp.next
    previous = None
    for _ in range(self.length):
      current = temp.next
      temp.next = previous
      previous = temp
      temp = current
      
      
    


ll = LinkList(3)
#ll.prepend(5)
ll.append(2)
ll.prepend(1)
ll.append(5)
#ll.popFirst()
#print(ll.get(2))
ll.setValue(1,9)
ll.insert(3,10)
ll.remove(1)

ll.printList()
ll.reverse()
ll.printList()
#ll.pop()
#print(ll.printList())
#ll.pop()
#print(ll.printList())
