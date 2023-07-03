## Given a binary tree, flatten it into linked list in-place. Usage of auxiliary data structure is not allowed. 
## After flattening, left of each node should point to NULL and right should contain next node in inorder.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def flatten(root):
    
    if(root == None or root.left == None or root.right == None):
        return
    
    if(root.left != None):
        flatten(root.left)
        # If root.left exists then we have
        # to make it root.right
        tempNode = root.right
        root.right = root.left
        root.left = None
        
        t = root.right
        while (t.right != None):
            t = t.right
            
        t.right = tempNode
    
    flatten(root.right)
        
def inorder(root):
    if(root == None):
        return
        
    inorder(root.left)
    print(root.data)
    inorder(root.right)
    
        

root = Node(1)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.right = Node(6)

flatten(root)
print("The Inorder traversal after flattening binary tree ")
inorder(root)