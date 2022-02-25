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

#Add first node.
first = Node(10)
#linking with head node
MyList.head = first
#linking next of the node with head
first.next = MyList.head

#Add second node.
second = Node(20)
#linking with first node
first.next = second
#linking next of the node with head
second.next = MyList.head