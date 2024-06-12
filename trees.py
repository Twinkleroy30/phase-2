class Box:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def printInOrderTraversal(root):
    if root==None:
        return
    printInOrderTraversal(root.left)
    print(root.data,end=" ")
    printInOrderTraversal(root.right)

def printPreOrderTraversal(root):
    if root==None:
        return
    print(root.data,end=" ")
    printPreOrderTraversal(root.left)
    printPreOrderTraversal(root.right)

def printPostOrderTraversal(root):
    if root==None:
        return 
    printInOrderTraversal(root.left)
    printInOrderTraversal(root.right)
    print(root.data,end=" ")


def printlevelOrderTraversal(root):
    if root == None:
        return 
    result = []
    Q = [root]
 
    while len(Q) > 0:
        n = len(Q)
        subResult = []
        for i in range(n):
            # step - 1
            currNode = Q.pop(0)
 
            # step - 2
            subResult.append(currNode.data)
 
            # step - 3
            if currNode.left != None:
                Q.append(currNode.left)
 
            # step - 4
            if currNode.right != None:
                Q.append(currNode.right)
 
        result.append(subResult)
 
    print(result)
 

    

obj1=Box(10)
obj2=Box(20)
obj3=Box(30)
obj4=Box(40)
obj5=Box(50)
obj6=Box(60)

obj1.left=obj2
obj1.right=obj3
obj2.left=obj4
obj2.right=obj5
obj3.left=obj6

print("InOrderTraversal")
printInOrderTraversal(obj1)
print("\nPreOrderTraversal")
printPreOrderTraversal(obj1)
print("\nPostOrderTraversal")
printPostOrderTraversal(obj1)
print("\nlevelOrderTraversal")
printlevelOrderTraversal(obj1)

