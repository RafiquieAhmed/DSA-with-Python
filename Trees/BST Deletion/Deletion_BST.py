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
    
def Delete(root,value):
    if(root ==value):
        return root
    if(root.data> value):
        root.left = Delete(root.left,value)
    elif(root.data<value):
        root.right=Delete(root.right,value)
    else:
        if(root.left ==None):
            return root.right
        if(root.right ==None):
            return root.left
        else:
            succ=get_successor(root)
            root.data=succ.data
            root.right=Delete(succ,succ.data)
    return root
def get_successor(root):
    root=root.right
    while(root!= None and root.left != None):
        root=root.left
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
# search(root,50)
# search(root,517)
Delete(root,5)

inorder(root)