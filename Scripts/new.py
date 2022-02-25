#constructor to create a new node
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

#class Linked List
class LinkedList:
  #constructor to create an empty LinkedList
  def __init__(self):
    self.head = None

# test the code    
# create an empty LinkedList                 
MyList = LinkedList()