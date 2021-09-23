class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

# A Linked List class with a single head node
class LinkedList:
	def __init__(self):
		self.head = None
		self.lenght = 0
		#self.tail = None

	def append(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			self.lenght += 1
			return

		last = self.head
		while(last.next):
			last = last.next
		
		last.next = new_node
		self.lenght += 1
		
		return self

	def preappend(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node
		self.lenght += 1

		return self

	def insert(self, index, data):
		new_node = Node(data)
		if index > self.lenght:
			self.append(data)
		leader = self.traverse_to_index(index-1)
		holding = leader.next
		leader.next = new_node
		new_node.next = holding
		self.lenght += 1

		return self
	
	def remove(self, index):
		if index == 0:
			leader = self.head
			self.head = leader.next
			
		elif index >= self.lenght:
			leader = self.traverse_to_index(index-1)
			leader.next = None
		else:
			leader = self.traverse_to_index(index-1)
			unwanted = leader.next
			leader.next = unwanted.next

		self.lenght -= 1
		return self

	def traverse_to_index(self, index):
		counter = 0
		current = self.head
		while(counter != index):
			current = current.next
			counter += 1
		return current
    			

	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next
    			

if __name__ == '__main__':
	ll = LinkedList()
	ll.append(1)
	ll.insert(1, 2)
	ll.append(3)
	ll.preappend(0)
	ll.append(4)
	ll.printList()
	print(ll.lenght)
	print('\n')
	ll.remove(5)
	ll.printList()
	print(ll.lenght)
	