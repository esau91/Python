class Stack:
    def __init__(self):
        self.array = []
    
    def peek(self):
        print(self.array[-1])

    def push(self, value):
        self.array.append(value)
        return self

    def pop(self):
        if len(self.array) >= 1:
            self.array.pop(-1)
        else:
            return None
        return self

my_stack = Stack()
my_stack.push(1)
my_stack.peek()
my_stack.push(2)
my_stack.peek()
my_stack.push(3)
my_stack.peek()
print(len(my_stack.array))
my_stack.pop()
my_stack.peek()
my_stack.pop()
my_stack.peek()
my_stack.pop()
print(len(my_stack.array))
my_stack.pop()