class Node:
    def __init__(self,value=None):
        self.data=value
        self.next=None
        self.prev=None

class DoubleLL:
    def __init__(self):
        self.head=None
        
    def insertAtEnd(self,value):
        temp=Node(value)
        if(self.head == None):
            self.head =temp
            return
        
        t =self.head
        while(t.next !=None):
            t=t.next
        t.next=temp
        temp.prev=t
    
    #inset Beigining
    def insertATbeginDLL(self,value):
        temp=Node(value)
        if(self.head==None):
            self.head=temp
            return
        temp.next=self.head
        self.head.prev=temp
        self.head=temp
            
            #insert at middle using searching
    def insertAtMiddel(self,value,x):
        t=self.head
        while(t.next !=None):
            if(t.data ==x):
                break
            else:
                t=t.next
        temp=Node(value)
        temp.next =t.next
        t.next.prev=temp
        t.next=temp
        temp.prev=t
        
                
                
                
    def printLL(self):
        t1=self.head
        while(t1.next !=None):
            print(t1.data,end="<-->")
            t1=t1.next
        print(t1.data)

obj=DoubleLL()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(50)
obj.insertATbeginDLL(5)
obj.insertAtMiddel(50,20)
obj.printLL()
            
        