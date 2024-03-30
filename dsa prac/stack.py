class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Peek from empty stack")
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
stack= Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Size of stack",stack.size())
print("Top element:", stack.peek())
print("Top element:", stack.peek())
while not stack.is_empty():
    print("Popped:", stack.pop())