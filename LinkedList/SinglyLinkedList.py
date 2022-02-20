""" 
******************************************************************************************************************

                        SINGLY LINKED LIST

    SOME NOTES:
    - Generally better to use a while loop instead of a for loop since you can do things like while(next != null)


******************************************************************************************************************
"""

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

    # Function to traverse and print contents of LinkedList
    # Start from head
    def printLinkedList(self):
        
        temp = self.head

        if (temp != None):
            print ("The list contains: ", end=" ")
            while (temp):
                print (temp.data, end= " ")
                temp = temp.next
            print('\n')
        else:
            print("The list is empty")

    # Function to count the number of nodes in a LinkedList
    # Recursively given 'node' as the starting node.
    def getSizeRecur(self, node):
        if (not node):
            return 0
        else: 
            return 1 + self.getSizeRecur(node.next)

    # Function to count the number of nodes in a LinkedList
    # Wrapper over getSizeRecur() function
    # Alternate solution is to add a count attribute to LinkedList class
    # and incrementing count whenever a node is inserted/deleted
    def getSize(self):
        return self.getSizeRecur(self.head)

    # Function to reverse a LinkedList
    def reverse(self):
        
        prev = None
        curr = self.head

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev 

    # Function that recursively searches for a given key in a LinkedList
    # Return true if key is present or false otherwise
    def searchRec(self, node, key):

        # Base case:
        # If head is NULL return false
        if (not node):
            return False

        # If key found return True
        if (node.data == key):
            return True

        # Recur through remaining list
        return self.searchRec(node.next, key)
    
    # Function that recursively searches for a given key in a LinkedList
    # Wrapper over searchRecur() function
    def search(self, key):
        return self.searchRec(self.head, key)

    # Function to return the data value stored at a given index
    # Recur through the LL
    def getIndexData(self, index):

        counter = 0
        curr = self.head

        while (curr.next):
            if (counter == index):
                return curr.data
            curr = curr.next
            counter += 1
        
        assert (False)
        return 0

    # Function to insert a node at the beginning of the LinkedList
    def push(self, newData):
        
        # Allocate the node and put in the data
        newNode = Node(newData)

        # Set next of new node to be head of LinkedList
        # Set the head to be new node
        newNode.next = self.head
        self.head = newNode

    # Funciton to insert a node after a given node in the LinkedList
    # Time complexity O(1)
    def insertAfter(self, prevNode, newData):
        
        # Allocate the node and put in the data
        newNode = Node(newData)

        # Set the next of newNode as the next of prevNode        
        # Set the next of prevNode as the newNode
        newNode.next = prevNode.next
        prevNode.next = newNode

    # Function to insert a node at the end of the LinkedList
    # Time complexity is O(n) where:
    #   n is the number of nodes in the LL
    # Since we are looping through the entire LL once, the function does O(n) work
    def append(self, newData):

        # Allocate the node and put in the data
        # Set the next of newNode as null/None (already done during instantiation)
        newNode = Node(newData)

        # If the LL is empty, set the head of the LL as the newNode
        if self.head is None:
            self.head = newNode
            return

        # Traverse to the last node of the LinkedList
        # Set the next pointer of the last node to newNode
        last = self.head
        while (last.next):
            last = last.next
        
        last.next = newNode

    # Function to delete a node given a key from the LinkedList
    # Given a reference to the head of the LL and a key, delete first occurance of key in the LL
    # Time complexity is O()
    def deleteNodeKey(self, key):

        # Store the head node
        curr = self.head  

        # Case where head node contains the key to be deleted
        if (curr is not None):
            if (curr.data == key):
                self.head = curr.next
                curr = None
                return 

        # Traverse through the LL and search for an occurance of the key
        # Keep track of the previous node as we need to change prev.next
        while (curr is not None):
            if (curr.data == key):
                break
            prev = curr  
            curr = curr.next

        # Key is not present in the LL
        if (curr == None):
            return
        
        # Unlink the node from the LL
        prev.next = curr.next
        curr = None

    # Function to delete a node given a position from the LinkedList
    def deleteNodePosition(self, position):

        # If LinkedList is empty do nothing
        if (self.head is None):
            return

        # If position given speicifies the head of the LL, set the head to the next node
        if (position == 0):
            self.head = self.head.next
            return self.head

        #
        index = 0
        curr = self.head
        prev = self.head
        while (curr is not None):
            if (index == position):
                prev.next = curr.next
                return prev
            prev = curr
            curr = curr.next
            index += 1

    # Function to delete a LinkedList
    # Alternatively, self.head = None would also delete the LinkedList due to python garbage collection
    def deleteLinkedList(self):
        
        # Store the head node
        curr = self.head 

        # Iterate through LinkedList
        while (curr is not None):
            
            # Store next node
            temp = curr.next

            # Delete the current node
            del curr.data

            # Set the curent node as temp (next node)
            curr = temp

            self.head = None

# Recursively reverse a Linked List
"""
def reverseRec(self, node, prev=None):
    if (node == None):
        self.head = prev
    
    if (node.next == None):
        return node

    node1 = reverse(node.next)
    node.next.next = node
    node.next = None
    return node1
"""

# Execute main
if __name__ == '__main__':

    # ***************************************************************


    print ('\n' + "TEST NUMBER 1: INITIALISE EMPTY LL" + '\n')

    # Initialise empty linked list
    ll = LinkedList()

    ll.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    '''
    Three nodes have been created.
    We have references to these three blocks as head,
    second and third
 
    ll.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  | None |     | 2  | None |     |  3 | None |
    +----+------+     +----+------+     +----+------+
    '''

    ll.head.next = second

    '''
    Now next of first Node refers to second.  So they
    both are linked.
 
    ll3.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  | null |     |  3 | null |
    +----+------+     +----+------+     +----+------+
    '''

    second.next = third

    '''
    Now next of second Node refers to third.  So all three
    nodes are linked.
 
    ll3.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  |  o-------->|  3 | null |
    +----+------+     +----+------+     +----+------+
    '''

    ll.printLinkedList()


    # ***************************************************************

    print("*"*50)
    print ('\n' + "TEST NUMBER 2: PUSH (insert at head) AND APPEND (insert at tail)" + '\n')

    # Initialise emptyList
    ll2 = LinkedList()

    # Insert 1. LL becomes 1->None
    ll2.push(1)

    # Insert 2 at the end. LL becomes 1->2->None
    ll2.append(2)

    # Insert 3 at the start. LL becomes 3->1->2->None
    ll2.push(3)

    ll2.printLinkedList()


    # ***************************************************************

    print("*"*50)
    print ('\n' + "TEST NUMBER 3: DELETE NODE GIVEN KEY" + '\n')

    # Initialise emptyList
    ll3 = LinkedList() 

    # Insert nodes into List
    ll3.push(7) 
    ll3.push(1) 
    ll3.push(3) 
    ll3.push(2) 

    print ("Created Linked List: ")
    ll3.printLinkedList() 
    ll3.deleteNodeKey(1) 
    print ("\nLinked List after Deletion of 1:")
    ll3.printLinkedList() 
    ll3.deleteNodeKey(7) 
    print ("\nLinked List after Deletion of 7:")
    ll3.printLinkedList() 


    # ***************************************************************

    print("*"*50)
    print ('\n' + "TEST NUMBER 4: DELETE NODE GIVEN POSITION" + '\n')

    # Initialise emptyList
    ll4 = LinkedList() 

    # Insert nodes into List
    ll4.push(7) 
    ll4.push(1) 
    ll4.push(3) 
    ll4.push(2) 

    print ("Created Linked List: ")
    ll4.printLinkedList()
    ll4.deleteNodePosition(3)
    print ("\nLinked List after Deletion at position 3: ")
    ll4.printLinkedList()

    ll4.deleteNodePosition(0)
    print ("\nLinked List after Deletion at position 0: ")
    ll4.printLinkedList()

    print ("\nSize of List is: ")
    print(ll4.getSize())


    # ***************************************************************

    print("*"*50)
    print ('\n' + "TEST NUMBER 5: DELETE LINKED LIST " + '\n')
    
    # Initialise emptyList
    ll5 = LinkedList() 

    # Insert nodes into List
    ll5.push(7) 
    ll5.push(1) 
    ll5.push(3) 
    ll5.push(2) 

    print ("Created Linked List: ")
    ll5.printLinkedList()

    ll5.deleteLinkedList()
    print ("\nLinked List after deletion")
    ll5.printLinkedList()

    print ("\nSize of List is: ")
    print(ll5.getSize())


 # ***************************************************************

    print("*"*50)
    print ('\n' + "TEST NUMBER 6: SEARCH FOR VALUE IN LL " + '\n')
    
    # Initialise emptyList
    ll6 = LinkedList() 

    # Insert nodes into List
    ll6.push(7) 
    ll6.push(1) 
    ll6.push(3) 
    ll6.push(2) 

    print ("Created Linked List: ")
    ll6.printLinkedList()

    print ("\nIs 4 in LL?: ")
    print(ll6.search(4))

    print ("\nIs 7 in LL?: ")
    print(ll6.search(7))


 # ***************************************************************

    print("*"*50)
    print ('\n' + "TEST NUMBER 6: REVERSE A LL" + '\n')
    
    # Initialise emptyList
    ll7 = LinkedList() 

    # Insert nodes into List
    ll7.push(7) 
    ll7.push(1) 
    ll7.push(3) 
    ll7.push(2) 

    print ("\nLL before reverse: ")
    ll7.printLinkedList()

    print ("\nLL after reverse: ")
    ll7.reverse()
    ll7.printLinkedList()


 # ***************************************************************
