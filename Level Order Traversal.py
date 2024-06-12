class Box:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
#left to right traversal
def levelOrderTraversal(root):
    if root==None:
        return
    result=[]
    Q=[root]
    while len(Q)>0:
        n=len(Q)
        subResult=[]
        for i in range(n):
            #step1
            currNode = Q.pop(0)
            #step2
            subResult.append(currNode.data)
            #step3
            if currNode.left!=None:
                Q.append(currNode.left)
            #step4
            if currNode.right!=None:
                Q.append(currNode.right)
        result.append(subResult)
    
    # Print the result
    print(result) 

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

print("LevelOrder Traversal:")
levelOrderTraversal(obj1)


# output
# LevelOrder Traversal:
# [[10], [20, 30], [50], [90, 80], [100]]