# Initialise the Node
class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

# Class for doubly Linked List
class doublyLinkedList:
    def __init__(self):
        self.start_node = None

# Inseart Emptylist
    def insert_in_emptylist(self,data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("list is not empty")

# Insert start
    def insert_at_start(self,data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node