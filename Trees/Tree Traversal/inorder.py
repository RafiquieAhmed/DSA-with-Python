class Node:
    def __init__(self,value):
        self.left =None
        self.right=None
        self.data=value
    
def InOrder(root):
    if( root != None):
        InOrder(root.left)
        print(root.data,end=" ")
        InOrder(root.right)
    

root=Node(1)
root.left =Node(3)
root.right =Node(5)
root.left.left =Node(2)
root.left.right =Node(4)
root.right.right=Node(8)
InOrder(root)