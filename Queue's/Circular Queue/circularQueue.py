class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.items=[None]*size
        self.front=self.rear = -1
        
    def EnQueue(self,value):
        if( (self.rear+1) % self.size == self.front):
            print("Queue is Full")
        elif(self.front==-1):
            self.front=self.rear=0
            self.items[self.rear]=value
        else:
            self.rear=(self.rear+1)%self.size
            self.items[self.rear]=value
    def Dequeue(self):
        if(self.front==-1):
            print("queue is empty")
        elif self.front ==self.rear:
            print(self.items[self.front])
            self.front =self.rear =-1
        else :
            print(self.items[self.front])
            self.front=(self.front+1)%self.size
    def display(self):
        print(self.items)

cd=CircularQueue(5)
cd.EnQueue(10)
cd.EnQueue(20)
cd.EnQueue(30)
cd.EnQueue(40)
cd.EnQueue(50)
cd.EnQueue(60)
cd.display()
cd.Dequeue()
cd.EnQueue(60)
cd.display()