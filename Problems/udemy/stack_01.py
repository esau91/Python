class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.lenght = 0
    
    def peek(self):
        top = self.top
        print(top.value)
        return self

    def push(self, value):
        new_node = Node(value)
        if self.lenght == 0:
            self.top = self.bottom = new_node
            self.lenght = 1
        else:
            new_node.next = self.top
            self.top = new_node
            self.lenght += 1
        return self

    def pop(self):
        if self.lenght == 0:
            return None
        self.top = self.top.next
        self.lenght -= 1
        return self

my_stack = Stack()
my_stack.push(1)
my_stack.peek()
my_stack.push(2)
my_stack.peek()
my_stack.push(3)
my_stack.peek()
print(my_stack.top.value)
my_stack.pop()
my_stack.peek()
print(my_stack.top.value)
my_stack.pop()
my_stack.peek()
print(my_stack.top.value)
my_stack.pop()
print(my_stack.lenght)