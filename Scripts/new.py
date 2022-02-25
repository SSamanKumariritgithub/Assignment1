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

#Add third node.
third = Node(30)
#linking with second node
second.next = third
#linking next of the node with head
third.next = MyList.head

 #display the content of the list
def PrintList(self):
    temp = self.head
    if(temp != None):
      print("The list contains:", end=" ")
      while (True):
        print(temp.data, end=" ")
        temp = temp.next
        if(temp == self.head):
          break
      print()
    else:
      print("The list is empty.")

# test the code   
# create an empty LinkedList                 
MyList = LinkedList()

#Add first node.
first = Node(10)
#linking with head node
MyList.head = first
#linking next of the node with head
first.next = MyList.head
