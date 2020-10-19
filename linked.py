class Node:
    def __init__(self, data, nextNode = None):
        self.data = data
        self.nextNode = nextNode


node1 = Node(3)
node2 = Node(7)
node3 = Node(10)
node4 = Node(77)
node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4

currentNode = node1

while True:
    print(f"{currentNode.data} -> ")
    if currentNode.nextNode is None:
        print("None")
        break
    currentNode = currentNode.nextNode

#second way to code a linked list


#first we create a node class
#this node class has the data of the node, and a pointer to the next node 
class LinkedListNode:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

#actual linked list class 
#this contains a head that we default to none
class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, data):
        node = LinkedListNode(data)
        if self.head is None:
            self.head = node
            return
        
        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode

    def printLinked(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.nextNode
        print("none")

ll = LinkedList()

ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.printLinked()