
class Stack:
    
    def __init__(self):
        self.list = []
        for i in range(0,2):
            self.list.append(i)
        self.top = -1
        
    def push(self,x):
        self.top = self.top+1
        self.list.insert(self.top,x)
        
    def pop(self):
        if(self.top>=0):
            self.top = self.top-1
        
    
    def peek(self):
        return self.list[self.top]
    
    def isEmpty(self):
        if(self.top == -1):
            return True
        else:
            return False
        
        
class Queue:
    
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        
        
    def enqueue(self,x):
        
        self.stack1.push(x)
        
    def dequeue(self):
        
        if (self.stack2.isEmpty() == True):
            
            while(not self.stack1.isEmpty()):
                self.stack2.push(self.stack1.peek())
                self.stack1.pop()
                
            self.stack2.pop()
            
        else:
            self.stack2.pop()
            
            
            
    def peek(self):
        if (self.stack2.isEmpty() == True):
            
            while(not self.stack1.isEmpty()):
                self.stack2.push(self.stack1.peek())
                self.stack1.pop()
                
            return self.stack2.peek()
            
        else:
            return self.stack2.peek()
        
        
        
        
        
        
        
def main():
    
    queue = Queue()
    total = int(input())
    
    for i in range(0,total):
        queryList = input().split(' ')
        
        if(int(queryList[0]) == 1):
            queue.enqueue(int(queryList[1]))
            
            
        if(int(queryList[0]) == 2):
            queue.dequeue()
            
        if(int(queryList[0]) == 3):
            print(queue.peek())
            
            
            
            
main()
            
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        