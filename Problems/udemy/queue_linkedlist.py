class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.lenght = 0
    
    def peek(self):
        my_first = self.first
        print(my_first.value)

    def enqueue(self, value):
        new_node = Node(value)
        if self.lenght == 0:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.lenght += 1
        return self

    def dequeue(self):
        if self.lenght == 0:
            return None
        else:
            self.first = self.first.next
            
        self.lenght -= 1
        return self

my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.peek()
print(my_queue.lenght)
my_queue.dequeue()
my_queue.peek()
print(my_queue.lenght)
my_queue.dequeue()
my_queue.peek()
print(my_queue.lenght)
my_queue.dequeue()
print(my_queue.lenght)