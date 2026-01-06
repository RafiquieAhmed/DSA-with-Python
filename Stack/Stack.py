class stack:
    def __init__(self):
        self.s=[]
    
    def s_length(self):
        return len(self.s)
    
    #push to create or insert element
    def push(self,value):
        self.s.insert(0,value)
        
    
    def peek(self):
        if(len(self.s)==0):
            raise Exception("Stack is empty")
        else :
            return self.s[0]
    
    #Pop delete element
    def pop(self):
        if(len(self.s)==0):
            raise Exception("Stack is empty")
        else :
            return self.s.pop(0)
    def Print_stack(self):
        print(self.s)
        
        
        
stk=stack()
stk.push(10)
stk.push(20)
stk.push(30)
stk.Print_stack()

print(stk.peek())
print(stk.pop())
print(stk.pop())
print(stk.pop())
