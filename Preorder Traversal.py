class Box:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

'''pre-order traversal  root->left->right'''

def printPreOrderTraversal(root):
    if root==None:
        return
    print(root.data,end=" ")
    printPreOrderTraversal(root.left)
    printPreOrderTraversal(root.right)

#object creation is happening here
obj1=Box(10)
obj2=Box(20)
obj3=Box(30)
obj4=Box(40)
obj5=Box(50)
obj6=Box(60)
obj7=Box(70)
obj8=Box(80)
obj9=Box(90)
obj10=Box(100)

#establishing links among these nodes
obj1.left=obj2
obj1.right=obj3
obj2.right=obj4
obj2.right=obj5
obj4.right=obj6
obj6.left=obj7
obj5.right=obj8
obj5.left=obj8
obj5.left=obj9
obj9.right=obj10

print("\nPre Order Traversal:")
printPreOrderTraversal(obj1)


# output
# Pre Order Traversal:
# 10 20 50 90 100 80 30

