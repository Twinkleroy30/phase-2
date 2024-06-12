def bottomViewHelper(root, store, hd, level):
    if root == None:
        return 
 
    if hd not in store or store[hd][0] < level:
        store[hd] = [level, root.data]
 
    bottomViewHelper(root.left, store, hd - 1, level + 1)
    bottomViewHelper(root.right, store, hd + 1, level + 1)
 
def findBottomView(root):
    result = []
    if root == None:
        return result
 
    store = {}
    bottomViewHelper(root, store, 0, 0)
    sortedKeys = sorted(store.keys())
    for key in sortedKeys:
        result.append(store[key][1])
    return result
 

 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 