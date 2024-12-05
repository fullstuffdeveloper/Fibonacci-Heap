import math
from .node import Node

import math

class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.node_count = 0
        self.node_map = {}  # Add this

    # Insert a new node with the given key
    def insert(self, key):
        new_node = Node(key)
        self.node_map[key] = new_node  # Add the node to the map
        if key < 0:
            raise ValueError("Error: Only positive numbers are allowed.")
        if self._key_exists(key):
            raise ValueError(f"Error: Duplicate keys are not allowed. Duplicate Key: {key}")    
        node = Node(key)
        self.node_map[key] = new_node  # Add to node_map
        if self.min_node is None:
            # First node, initialize the heap
            self.min_node = node
        else:
            # Add the new node to the root list
            node.left = self.min_node
            node.right = self.min_node.right
            self.min_node.right = node
            node.right.left = node
            # Update min_node if needed
            if node.key < self.min_node.key:
                self.min_node = node
        self.node_count += 1
        return node

    # Return the node with the minimum key
    def find_min(self):
        return self.min_node

    # Remove the node with the minimum key and restructure the heap
    def extract_min(self):
        z = self.min_node
        if z is not None:
            # Make each child of z a root
            if z.child is not None:
                children = []
                child = z.child
                while True:
                    children.append(child)
                    child = child.right
                    if child == z.child:
                        break
                for child in children:
                    child.left.right = child.right
                    child.right.left = child.left
                    child.left = self.min_node
                    child.right = self.min_node.right
                    self.min_node.right = child
                    child.right.left = child
                    child.parent = None
            # Remove z from the root list
            z.left.right = z.right
            z.right.left = z.left
            if z == z.right:
                self.min_node = None
            else:
                self.min_node = z.right
                self._consolidate()
            self.node_count -= 1
        return z

    # Consolidate the heap by linking trees of the same degree
    def _consolidate(self):
        max_degree = int(math.log(self.node_count) * 1.44) + 1
        A = [None] * max_degree
        roots = []
        x = self.min_node
        if x is not None:
            while True:
                roots.append(x)
                x = x.right
                if x == self.min_node:
                    break
            for w in roots:
                x = w
                d = x.degree
                while A[d] is not None:
                    y = A[d]
                    if x.key > y.key:
                        x, y = y, x
                    self._link(y, x)
                    A[d] = None
                    d += 1
                A[d] = x
        # Rebuild the root list and find the new min node
        self.min_node = None
        for i in range(max_degree):
            if A[i] is not None:
                if self.min_node is None:
                    self.min_node = A[i]
                    A[i].left = A[i]
                    A[i].right = A[i]
                else:
                    A[i].left = self.min_node
                    A[i].right = self.min_node.right
                    self.min_node.right = A[i]
                    A[i].right.left = A[i]
                    if A[i].key < self.min_node.key:
                        self.min_node = A[i]

    # Link two trees of the same degree
    def _link(self, y, x):
        y.left.right = y.right
        y.right.left = y.left
        y.parent = x
        if x.child is None:
            x.child = y
            y.left = y
            y.right = y
        else:
            y.left = x.child
            y.right = x.child.right
            x.child.right = y
            y.right.left = y
        x.degree += 1
        y.mark = False

    # Decrease the key of a specific node
    # Decrease the key of a specific node
    def decrease_key(self, key, new_key):
        """Decrease the key of a specific node."""
        print(f"Decreasing key {key} to {new_key}")

        # Ensure the key exists
        if key not in self.node_map:
            raise ValueError(f"Key {key} not found in the heap.")
        if new_key >= key:
            raise ValueError("New key must be less than the current key.")

        # Retrieve the node and update its key
        node = self.node_map[key]
        del self.node_map[key]  # Remove the old key
        node.key = new_key  # Update the node's key
        self.node_map[new_key] = node  # Add the new key

        # Handle cascading cuts if needed
        parent = node.parent
        if parent and node.key < parent.key:
            print(f"Cutting node {node.key} from parent {parent.key}")
            self._cut(node, parent)
            self._cascading_cut(parent)

        # Update the minimum node if necessary
        if node.key < self.min_node.key:
            self.min_node = node

        print(f"Key {key} decreased to {new_key}.")






    def _remove_node(self, node):
        """Remove a node directly from the heap."""
        print(f"Removing node with key {node.key}")
        # Remove from parent's child list if necessary
        if node.parent:
            self._cut(node, node.parent)

        # Remove from root list
        node.left.right = node.right
        node.right.left = node.left

        # Update min_node if needed
        if node == self.min_node:
            if node.right == node:  # Single node case
                self.min_node = None
            else:
                self.min_node = node.right
                self._consolidate()

        self.node_count -= 1
        print(f"Node with key {node.key} successfully removed.")

    # Cut node x from its parent y
    def _cut(self, node, parent):
        """Cut `node` from its parent and add it to the root list."""
        # Remove the node from its sibling list
        if node.right == node:  # Only child case
            parent.child = None
        else:
            node.right.left = node.left
            node.left.right = node.right
            if parent.child == node:
                parent.child = node.right  # Update parent.child

        parent.degree -= 1

        # Add node to root list
        node.left = self.min_node
        node.right = self.min_node.right
        self.min_node.right = node
        node.right.left = node

        # Update node properties
        node.parent = None
        node.mark = False


    # Perform a cascading cut on node y
    def _cascading_cut(self, y):
        z = y.parent
        if z is not None:
            if not y.mark:
                y.mark = True
            else:
                self._cut(y, z)
                self._cascading_cut(z)

    # Delete a specific node from the heap
    # def delete(self, x):
    #     self.decrease_key(x, float('-inf'))
    #     self.extract_min()

    # Merge two Fibonacci heaps
    def merge(self, other_heap):
        if other_heap.min_node is None:
            return
        if self.min_node is None:
            self.min_node = other_heap.min_node
        else:
            # Concatenate the root lists
            self.min_node.right.left = other_heap.min_node.left
            other_heap.min_node.left.right = self.min_node.right
            self.min_node.right = other_heap.min_node
            other_heap.min_node.left = self.min_node
            if other_heap.min_node.key < self.min_node.key:
                self.min_node = other_heap.min_node
        self.node_count += other_heap.node_count

    def _key_exists(self, key):
        if self.min_node is None:
            return False
        # Rest of the method implementation goes here    start = self.min_node
        start = self.min_node
        node = start
        while True:
            if node.key == key:
                return True
            if node.child:
                if self._key_exists_in_subtree(node.child, key):
                    return True
            node = node.right
            if node == start:
                break
        return False
    def display_statistics(self):
        print("\nHeap Statistics:")
        print(f"Total nodes: {self.total_nodes}")
        print(f"Minimum key: {self.min_node.key if self.min_node else 'None'}")
        print(f"Number of roots: {len(self.root_list)}")
        print(f"Marked nodes: {sum(1 for node in self.node_map.values() if node.mark)}")

    def _key_exists_in_subtree(self, node, key):
            """Helper function to check for a key in a subtree."""
            start = node
            while True:
                if node.key == key:
                    return True
                if node.child:
                    if self._key_exists_in_subtree(node.child, key):
                        return True
                node = node.right
                if node == start:
                    break
            return False
    def _display_tree(self, node, indent=0):
        if node is None:
            return ""
        
        result = "  " * indent + f"{node.key} {'(min)' if node == self.min_node else ''}\n"
        
        # Traverse the children
        if node.child:
            child = node.child
            while True:
                result += self._display_tree(child, indent + 2)
                child = child.right
                if child == node.child:
                    break
        
        return result
    def delete(self, key):
        """Delete a node with the given key."""
        print(f"Attempting to delete key: {key}")
        
        # Ensure the key exists
        if key not in self.node_map:
            raise ValueError(f"Key {key} not found in the heap.")
        
        # Retrieve the node to be deleted
        node = self.node_map[key]
        print(f"Node found: {node.key}. Decreasing key to -inf for removal.")
        
        # Decrease the key to -inf
        self.decrease_key(key, float('-inf'))
        
        # Extract the minimum node
        extracted_node = self.extract_min()
        print(f"Extracted node: {extracted_node.key}. Expected node: -inf.")
        
        # Remove from node_map
        if key in self.node_map:
            del self.node_map[key]
        print(f"Key {key} successfully deleted.")





    def _iterate_root_list(self):
        if self.min_node is None:
            return
        current = self.min_node
        while True:
            yield current
            current = current.right
            if current == self.min_node:
                break

