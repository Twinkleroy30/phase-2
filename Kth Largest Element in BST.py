class Solution:
    def collectInOrderTraversal(self,root,arr):
        if root==None:
            return
        self.collectInOrderTraversal(root.left,arr)
        arr.append(root.data)
        self.collectInOrderTraversal(root.right,arr)
    def kthLargest(self,root, k):
        #your code here
        arr=[]
        self.collectInOrderTraversal(root,arr)
        n=len(arr)
        return arr[n-k]