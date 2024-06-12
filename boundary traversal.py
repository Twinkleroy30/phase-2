def isLeafNode(root):
    if root.left == None and root.right == None:
        return True 
    return False
 
def collectLeftView(root, result):
    if root == None:
        return 
    while root != None and isLeafNode(root)== False:
        result.append(root.data)
        if root.left != None:
            root = root.left 
        else:
            root = root.right
 
def collectLeafNodes(root, result):
    if root == None:
        return 
    elif isLeafNode(root):
        result.append(root.data)
        return  
    collectLeafNodes(root.left, result)
    collectLeafNodes(root.right, result)
 
 
 
def collectRightViewInReverseFashion(root, result):
    if root == None:
        return 
    temp = []
    while root != None and isLeafNode(root)== False:
        temp.append(root.data)
        if root.right != None:
            root = root.right 
        else:
            root = root.left
    temp = temp[::-1]
    for ele in temp:
        result.append(temp)
 
def findBoundaryTraversal(root):
    if root == None:
        return []
    result = []
    result.append(root.data)
 
    collectLeftView(root.left, result)
    collectLeafNodes(root, result)
    collectRightViewInReverseFashion(root.right, result)
    return result
 