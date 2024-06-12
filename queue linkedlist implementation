# Linked list implementation of Queue


class Box:
    def __init__(self, data):
        self.data = data 
        self.next = None
 
def printLinkedList(curr):
    if curr == None:
        print("Empty Linked list")
        return
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next 
    print()
 
def enQueue(head, ele):
    temp = Box(ele) 
    if head == None:
        return temp
    tail = head 
 
    while tail.next != None:
        tail = tail.next 
    tail.next = temp
    return head 
 
 
def deQueue(head):
    if head == None:
	    return None 
    secondNode = head.next 
    head.next = None 
    return secondNode
 
queueHead = None 
printLinkedList(queueHead)
queueHead = enQueue(queueHead, 34)
queueHead = enQueue(queueHead, 35)
queueHead = enQueue(queueHead, 36)
queueHead = enQueue(queueHead, 37)
printLinkedList(queueHead)
queueHead = deQueue(queueHead)
printLinkedList(queueHead)
queueHead = deQueue(queueHead)
printLinkedList(queueHead)
 
 
 
 
# Empty Linked list
# 34 --> 35 --> 36 --> 37 --> 
# 35 --> 36 --> 37 --> 
# 36 --> 37 --> 
 
 