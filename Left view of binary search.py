def findLeftView(root):
    if root == None:
        return []
    result = []
    Q = [root]
 
    while len(Q) > 0:
        n = len(Q)
        for i in range(n):
            curr = Q.pop(0)
            if i == 0:
                result.append(curr.data)
            if curr.left != None:
                Q.append(curr.left)
 
            if curr.right != None:
                Q.append(curr.right)
    return result