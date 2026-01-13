#bst insertion and seaching same nlogn for n no.of elements insert

class Node:
    def __init__(self,value):
        self.left= None
        self.right= None
        self.data =value
        
def insert(root,value):
        if(root ==None):
            return Node(value)
        if(root.data ==value):
            return root
        if(root.data >value):
            root.left=insert(root.left, value)
        else:
            root.right=insert(root.right,value)
        return root
    
def search(root,value):
        if(root ==None):
            print("not found",end="\n")
            return
        if(root.data ==value):
            print("found element",end="\n")
            return
        if(root.data >value):
            search(root.left, value)
        else:
            search(root.right,value)
        return root
    
def inorder(root):
    if(root!=None):
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
    
root= insert(None,20)
root =insert(root,15)
root =insert(root,4)
root =insert(root,5)
root =insert(root,65)
root =insert(root,95)
root =insert(root,50)
root =insert(root,115)
root =insert(root,125)
root =insert(root,1500)

inorder(root)
print("\n")
search(root,50)
search(root,517)