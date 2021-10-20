# # of nodes = 2 ^ hight - 1
# log nodes = hight
# Big(O) O(log N) (Balanced)
# Big(O) O(N) (Unbalanced)

class Node:
    def __init__(self, value):
        self.data = value
        self.right = None
        self.left = None

class binary_search_tree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        root = self.root
        if root is None:
            self.root = new_node
        else:
            current = root
            while(True):
                if value < current.data:
                    if not current.left:
                        current.left = new_node
                        return self
                    else:
                        current = current.left
                else:
                    if not current.right:
                        current.right = new_node
                        return self
                    else:
                        current = current.right
        
            '''
            while(current):
                tmp = current
                left = False

                if current.data > value:
                    current = current.left  
                    left = True
                else:
                    current = current.right
            if left:
                tmp.left = new_node
            else:
                tmp.right = new_node
            '''

    def lookup(self, value):
        if not self.root:
            return None
        current = self.root
        while(current):
            if current.data == value:
                print(current.data)
                return self
            elif value < current.data:
                current = current.left
            else:
                current = current.right
        return None
    
def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.data)
        printTree(node.right, level + 1)

tree = binary_search_tree()
tree.insert(9)
tree.lookup(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.lookup(1)
printTree(tree.root)