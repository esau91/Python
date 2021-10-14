class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None

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
			return self

		last = self.head
		while(last.next):
			last = last.next
		
		last.next = new_node
		new_node.prev = last
		self.lenght += 1
		
		return self

	def preappend(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head.prev = new_node
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
		new_node.prev = leader
		holding.prev = new_node

		self.lenght += 1

		return self
	
	def remove(self, index):
		if index == 0:
			leader = self.head
			self.head = leader.next
			self.head.prev = None
		elif index >= self.lenght:
			leader = self.traverse_to_index(index-1)
			leader.next = None
		else:
			leader = self.traverse_to_index(index-1)
			unwanted = leader.next
			leader.next = unwanted.next
			leader.next.prev = unwanted.prev

		self.lenght -= 1
		return self

	def traverse_to_index(self, index):
		counter = 0
		current = self.head
		while(counter != index):
			current = current.next
			counter += 1
		return current

	def reverse(self):
		current = self.head

		while(current):
			tmp = current.prev
			current.prev = current.next
			current.next = tmp
			current = current.prev
		
		if tmp:
			self.head = tmp.prev

		return self 			

	def printList(self):
		temp = self.head
		while(temp):
			if temp.next is None:
				print('data: {}, next: {}, prev: {}'.format(temp.data, None, temp.prev.data))
			elif temp.prev is None:
				print('data: {}, next: {}, prev: {}'.format(temp.data, temp.next.data, None))
			else:
				print('data: {}, next: {}, prev: {}'.format(temp.data, temp.next.data, temp.prev.data))
			temp = temp.next
    			

if __name__ == '__main__':
	ll = LinkedList()
	ll.append(1)
	ll.preappend(0)
	ll.append(3)
	ll.insert(2, 2)
	ll.append(4)
	ll.printList()
	print(ll.lenght)
	print('\n')
	ll.remove(2)
	ll.printList()
	print(ll.lenght)
	print('\n')
	ll.reverse()
	ll.printList()