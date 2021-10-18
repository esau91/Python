class Queue:
    def __init__(self):
        self.my_array = []
    
    def peek(self):
        print(self.my_array[-1])

    def enqueue(self, value):
        self.my_array.insert(0,value)

        return self

    def dequeue(self):
        self.my_array.pop(-1)
        return self

my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.peek()
print(len(my_queue.my_array))
my_queue.dequeue()
my_queue.peek()
print(len(my_queue.my_array))
my_queue.dequeue()
my_queue.peek()
print(len(my_queue.my_array))
my_queue.dequeue()
print(len(my_queue.my_array))