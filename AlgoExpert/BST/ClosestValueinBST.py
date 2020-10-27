class BST:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        #self.root = None
        #self.size = 0

    def length(self):
        return self.size
    
    def search(root,val): 
      
    # Base Cases: root is null or key is present at root 
        if root is None or root.val == val: 
            return root 
  
    # Key is greater than root's key 
        if root.val < val: 
            return search(root.right,val) 
    
    # Key is smaller than root's key 
        return search(root.left,val)
    
    def insert(self,value): 
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                else:
                    currentNode = currentNode.right
                
            
    def inorder(root): 
        if root: 
            inorder(root.left) 
            print(root.val) 
            inorder(root.right) 

# Driver program to test the above functions 
# Let us create the following BST 
#      50 
#    /      \ 
#   30     70 
#   / \    / \ 
#  20 40  60 80 
'''
r = Node(50) 
r.insert(r,Node(30)) 
r.insert(r,Node(20)) 
r.insert(r,Node(40)) 
r.insert(r,Node(70)) 
r.insert(r,Node(60)) 
r.insert(r,Node(80)) 
'''
r = BST(50)
#self.root = 50
#rootNode=r
r.insert(30) 
r.insert(20) 
r.insert(40) 
r.insert(70) 
r.insert(60) 
r.insert(80) 

  
# Print inoder traversal of the BST 
r.inorder(r) 
  