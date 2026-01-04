class Node:
    def __init__(self,info,next=None):
        self.data=info
        self.next=next
        
class SinglyLinkedList:
    def __init__(self,head=None): #pointer assine
        self.head=head
        
    def insertAtEnd(self,value):
        temp=Node(value)
        # if already create 
        if(self.head != None):
            new_Node=self.head
            while(new_Node.next !=None):
                new_Node=new_Node.next
            new_Node.next =temp
        
        # if not  created
        else:
            self.head=temp
            
            #print data
      
    def inserAtBegining(self,value):
        temp =Node(value)
        temp.next=self.head
        self.head=temp
        
    #insert at middle
    def insertInMid(self,value,x): 
        #x is searching element
        temp=Node(value)
        t1=self.head
        
        while(t1.next !=None):
            if(t1.data ==x):
                temp.next=t1.next
                t1.next =temp
            t1 =t1.next
            
            
    def deleteLL(self,value):
        t1=self.head
        prev=t1
        if(t1.data == value):
            self.head=t1.next
            #this block is ,middle ele
        while(t1.next != None):
            if(t1.data ==value):
                prev.next =t1.next
                break
            else:
                prev =t1
                t1= t1.next
        if(t1.data==value):
            prev.next=None
    
          
    def printLL(self):
        new_Node=self.head
        while(new_Node.next !=None):
            print(new_Node.data)
            new_Node=new_Node.next
        print(new_Node.data)
        
obj =SinglyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.inserAtBegining(5)
obj.insertInMid(40,20)
obj.deleteLL(30)
obj.printLL()

