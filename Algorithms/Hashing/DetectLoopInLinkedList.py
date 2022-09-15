# Python3 program to detect loop in
# given linked list using map
 
# Structure for a node in Linked List
class Node:
    def __init__(self, val):
        self.data = val
        self.Next = None
 
# Function to create Linked List Node
def newNode(d):
    temp = Node(d)
    return temp
 
# Declaration of Map to keep
# mark of visited Node
vis = {}
flag = False
 
# Function to check cycle in Linked
# List
def check(head):
    global vis, flag
    # If head is null return ;
    if head == None:
        flag = False
        return
 
    # Mark the incoming Node as
    # visited if it is not visited yet
    if head not in vis:
        vis[head] = True
        check(head.Next)
 
    # If a visited Node is found
    # Update the flag value to 1
    # and return ;
    else:
        flag = True
        return
 
# Create a head Node
head = newNode(20)
 
# Inserting Node in Linked List
head.Next = newNode(4)
head.Next.Next = newNode(5)
head.Next.Next.Next = newNode(10)
 
# Just to make a cycle
head.Next.Next.Next.Next = head
 
# Function that detect cycle in
# Linked List
check(head)
 
# If flag is true, loop is found
if flag:
    print("Loop detected.")
 
# If flag is false, No Loop
# detected
else:
    print("No Loop Found.")
     