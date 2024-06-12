

#6PW7zNfz

class Box:
    def __init__(self, data):
        self.data = data 
        self.next = None
 
def printLinkedList(curr):
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next 
    print()
 
def insertAtTailNode(head, ele):
    temp = Box(ele) 
    if head == None:
        return temp
    tail = head 
 
    while tail.next != None:
        tail = tail.next 
    tail.next = temp
    return head 

 
def insertAtBeginning(head, ele):
    temp = Box(ele)
    if head == None:
        return temp 
    temp.next = head 
    return temp
 
def insertAtSpecificPosition(head, position, ele):
    if position == 0:
        return insertAtBeginning(head, ele)
 
    temp = Box(ele)
    currentIndex = 0 
    currentNode = head 
    while currentIndex != position - 1:
        currentIndex += 1 
        currentNode = currentNode.next 
 
    temp.next = currentNode.next 
    currentNode.next = temp 
    return head
#delete tail node

def deleteTailnode(head):
    curr=head
    if curr==None or curr.next==None:
        return None
    while curr.next.next!=None:
        curr=curr.next
    curr.next=None
    return head
 
head = None
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for ele in nums:
    head =insertAtBeginning(head,ele)

printLinkedList(head)
head=deleteTailnode(head)
printLinkedList(head)


#DELETE AT SPECIFIC POSITUON

def deleteNodeAtSpecificPosition(head,position):
    if position==0:
        return deleteNodeAtSpecificPosition(head)
    currentindex=0
    currentnode=head
    while currentindex != position-1:
        currentindex+=1
        currentnode=currentnode.next
        nodeToBeDeleted=currentnode.next
        currentnode.next=nodeToBeDeleted.next
        nodeToBeDeleted.next=None
        return head
head = None
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for ele in nums:
    head =insertAtBeginning(head,ele)

printLinkedList(head)
head=deleteNodeAtSpecificPosition(head,2)
printLinkedList(head)






 
# printLinkedList(head)
# head = insertAtSpecificPosition(head, 5, 1899)
# printLinkedList(head)
 
# n = int(input())
# for i in range(n):
#     ele = int(input())
#     head = insertAtTailNode(head, ele)
 
 
 
 
 
# block creation is happening in below 4 lines      
#obj1 = Box(10)
#print("Printing address from main function", obj1)
# obj2 = Box(20)
# obj3 = Box(30)
# obj4 = Box(40) 
# establishing links in below 4 lines
# obj1.next = obj2 
# obj2.next = obj3 
# obj3.next = obj4 
# obj4.next = None 
 