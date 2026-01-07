class Queue:
    def __init__(self):
        self.items=[]
    
    #underflow  to check
    def isEmpty(self):
        return len(self.items)==0
    
    def insert(self,value):
        self.items.append(value)
        
    def delete(self):
        if(self.isEmpty()):
            print("queue is empty")
        else:
            return self.items.pop(0)
    def printqu(self):
        print(self.items)
qu=Queue()
qu.insert(10)
qu.insert(20)
qu.insert(30)
qu.printqu()

print(qu.delete())
print(qu.delete())   
print(qu.delete())    
print(qu.delete())    