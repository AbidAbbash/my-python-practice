#Defining the binary tree node class
class TreeNode:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
        
#Function to get breadth-first values using a queue

def bfv(root):
    if not root:
        return []
    queue = [root]   #Starting with the root node in queue
    result =[]
    
    while queue:
        current= queue.pop(0)  #Dequeue the front node. This pop(0) 0 was important
        result.append(current.value)
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result

# Create tree nodes
a = TreeNode('A')
b = TreeNode('B')
c = TreeNode('C')
d = TreeNode('D')
e = TreeNode('E')
f = TreeNode('F')

# Link the nodes
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

# Run bfv
print(bfv(a))