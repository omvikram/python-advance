## Given the root of a binary tree, display the node values at each level. Node values for all levels should be displayed on separate lines. 
## Level order traversal for this tree should look like:

## 100
## 50, 200
## 25, 75, 350

class TreeNode:
    def __init__(self, data):
        self.value = data
        self.left_child = None
        self.right_child = None
        
def printLevelOrderNodes(rootNode):
    ##calculate the height of the tree
    ##for each level of the height print the node values
    level = calculateHeightOfBTree(rootNode)
    
    for h in range(1, level+1):
        printNodes(rootNode, h)
    

def calculateHeightOfBTree(rootNode):
    
    if(rootNode == None):
        return 0
   
    left_height =  calculateHeightOfBTree(rootNode.left_child) 
    right_height = calculateHeightOfBTree(rootNode.right_child)
    
    if(left_height > right_height):
        return left_height + 1
    else:
        return right_height + 1
        
        
def printNodes(rootNode, level):
    if (rootNode == None):
        return
        
    if (level == 1):
        print(rootNode.value)
    elif (level > 1):
        printNodes(rootNode.left_child, level - 1)
        printNodes(rootNode.right_child, level - 1)
    
    
        
root = TreeNode(100) 
root.left_child = TreeNode(50) 
root.right_child = TreeNode(200) 
root.left_child.left_child = TreeNode(25) 
root.left_child.right_child = TreeNode(75)
root.right_child.left_child = TreeNode(350) 
   
printLevelOrderNodes(root)

    