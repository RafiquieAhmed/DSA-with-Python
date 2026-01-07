class Queue:
    def __init__(self):
        self.items=[]
    
    #underflow  to check
    def isEmpty(self):
        return len(self.items)==0
    
    def insertAtEnd(self,value):
        self.items.append(value)
        
    def DeleteATFront(self):
        if(self.isEmpty()):
            print("queue is empty")
        else:
            return self.items.pop(0)
        
    def insertAtBegin(self,value):
        self.items.insert(0,value)
    
    def DeleteAtEnd(self):
        if(self.isEmpty()):
            print("queue is empty")
        else:
            return self.items.pop()
    def printqu(self):
        
        print(self.items)
qu=Queue()
qu.insertAtEnd(10)
qu.insertAtBegin(20)
qu.insertAtEnd(30)
qu.insertAtEnd(40)
qu.insertAtBegin(50)
qu.printqu()
print(qu.DeleteAtEnd())
print(qu.DeleteAtEnd())
print(qu.deleteATFront())
print(qu.DeleteATFront())
print(qu.DeleteATFront())

