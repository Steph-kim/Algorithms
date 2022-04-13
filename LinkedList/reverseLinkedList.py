# Node Class
class Node:
    # Function to initialise the Node object
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    # Function to initialise the LinkedList object
    def __init__(self):
        self.head = None

# Recursively reverse a Linked List
def reverseRec1(node, prev=None):
    if (node == None):
        self.head = prev
    
    if (node.next == None):
        return node

    node1 = reverseRec1(node.next)
    node.next.next = node
    node.next = None
    return node1

# Function to reverse the linked list 
def reverseRec2(node):
    if (node == None):
        return node
          
    if (node.next == None):
        return node
          
    node1 = reverseRec2(node.next)
    node.next.next = node
    node.next = None
    return node1

# Iteratively reverse a linked list
def reverseList(head):
    if head == None:
        return head 
    prev = None
    curr = head
    
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev
    return head