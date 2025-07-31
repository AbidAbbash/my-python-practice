class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left= None
        self.right= None

#Function to perform depth first traversal (iterative using stack)
def depth_first_value(root):
    if root is None:
        return []
        
    stack=[root] #Initialize stack with root node
    result=[]  #This will hold our DFS traversal output
    
    while stack:
        current = stack.pop() #Pop the node from the stack
        result.append(current.value) #Process the current node
        
        #push righ child first so that left is processed first (stack=LIFO)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return result
    
a = TreeNode('A')
b = TreeNode('B')
c = TreeNode('C')
d = TreeNode('D')
e = TreeNode('E')
f = TreeNode('F')

a.left=b
a.right=c
b.left=d
b.right=e
c.right=f

print(depth_first_value(a))