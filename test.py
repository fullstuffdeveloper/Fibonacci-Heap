class FibonacciHeapNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.child = None
        self.left = self
        self.right = self
        self.degree = 0
        self.mark = False

class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.total_nodes = 0

    def display_heap(self):
        if self.min_node is None:
            print("Heap is empty!")
            return
        
        print("\nRoot List:")
        current = self.min_node
        first_pass = True
        while current != self.min_node or first_pass:
            first_pass = False
            children = [child.key for child in self._iterate(current.child)] if current.child else []
            print(f"Node Key: {current.key}, Degree: {current.degree}, Children: {children if children else 'None'}")
            current = current.right

        print(f"\nHeap Statistics:")
        print(f"Total nodes: {self.total_nodes}")
        print(f"Minimum key: {self.min_node.key if self.min_node else 'None'}")

    def insert(self, key):
        node = FibonacciHeapNode(key)
        if self.min_node is None:
            self.min_node = node
        else:
            self._merge_with_root_list(node)
            if node.key < self.min_node.key:
                self.min_node = node
        self.total_nodes += 1
        self.display_heap()
        return node

    def _merge_with_root_list(self, node):
        node.left = self.min_node.left
        node.right = self.min_node
        self.min_node.left.right = node
        self.min_node.left = node

    def extract_min(self):
        z = self.min_node
        if z is not None:
            if z.child:
                children = [child for child in self._iterate(z.child)]
                for child in children:
                    self._merge_with_root_list(child)
                    child.parent = None
            z.left.right = z.right
            z.right.left = z.left
            if z == z.right:
                self.min_node = None
            else:
                self.min_node = z.right
                self._consolidate()
            self.total_nodes -= 1
            self.display_heap()
            return z.key
        return None

    def _consolidate(self):
        max_degree = int(self.total_nodes ** 0.5) + 1
        degree_table = [None] * max_degree
        root_nodes = [node for node in self._iterate(self.min_node)]
        for node in root_nodes:
            degree = node.degree
            while degree_table[degree]:
                other = degree_table[degree]
                if node.key > other.key:
                    node, other = other, node
                self._link_nodes(node, other)
                degree_table[degree] = None
                degree += 1
            degree_table[degree] = node
        self.min_node = None
        for node in degree_table:
            if node:
                if not self.min_node or node.key < self.min_node.key:
                    self.min_node = node

    def _link_nodes(self, parent, child):
        child.left.right = child.right
        child.right.left = child.left
        child.parent = parent
        child.left = child.right = child
        if parent.child is None:
            parent.child = child
        else:
            child.left = parent.child.left
            child.right = parent.child
            parent.child.left.right = child
            parent.child.left = child
        parent.degree += 1
        child.mark = False

    def _iterate(self, start_node):
        if start_node is None:
            return []
        nodes = []
        current = start_node
        while True:
            nodes.append(current)
            current = current.right
            if current == start_node:
                break
        return nodes

    def decrease_key(self, node, new_key):
        if new_key > node.key:
            raise ValueError("New key must be less than current key")
        node.key = new_key
        parent = node.parent
        if parent and node.key < parent.key:
            self._cut(node, parent)
            self._cascading_cut(parent)
        if node.key < self.min_node.key:
            self.min_node = node
        self.display_heap()

    def _cut(self, node, parent):
        if node.right != node:
            node.right.left = node.left
            node.left.right = node.right
        if parent.child == node:
            parent.child = node.right if node != node.right else None
        parent.degree -= 1
        self._merge_with_root_list(node)
        node.parent = None
        node.mark = False

    def _cascading_cut(self, parent):
        grandparent = parent.parent
        if grandparent:
            if not parent.mark:
                parent.mark = True
            else:
                self._cut(parent, grandparent)
                self._cascading_cut(grandparent)

    def delete(self, node):
        self.decrease_key(node, float('-inf'))
        self.extract_min()

# Menu-Driven Program
fib_heap = FibonacciHeap()
node_map = {}  # To map keys to nodes for operations like decrease key and delete

while True:
    print("\nMenu:")
    print("1. Insert")
    print("2. Extract Min")
    print("3. Decrease Key")
    print("4. Delete Node")
    print("5. Display Heap")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        key = int(input("Enter key to insert: "))
        node = fib_heap.insert(key)
        node_map[key] = node
    elif choice == 2:
        print(f"Extracted Min: {fib_heap.extract_min()}")
    elif choice == 3:
        key = int(input("Enter the key of the node to decrease: "))
        new_key = int(input("Enter the new key (must be smaller): "))
        if key in node_map:
            fib_heap.decrease_key(node_map[key], new_key)
            del node_map[key]
            node_map[new_key] = node_map.get(new_key)
        else:
            print("Key not found!")
    elif choice == 4:
        key = int(input("Enter the key of the node to delete: "))
        if key in node_map:
            fib_heap.delete(node_map[key])
            del node_map[key]
        else:
            print("Key not found!")
    elif choice == 5:
        fib_heap.display_heap()
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
