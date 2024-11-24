import math
from .node import Node

import math

class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.node_count = 0

    # Insert a new node with the given key
    def insert(self, key):
        node = Node(key)
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
    def decrease_key(self, x, k):
        if k > x.key:
            raise ValueError("new key is greater than current key")
        x.key = k
        y = x.parent
        if y is not None and x.key < y.key:
            self._cut(x, y)
            self._cascading_cut(y)
        if x.key < self.min_node.key:
            self.min_node = x

    # Cut node x from its parent y
    def _cut(self, x, y):
        if x.right == x:
            y.child = None
        else:
            x.right.left = x.left
            x.left.right = x.right
            if y.child == x:
                y.child = x.right
        y.degree -= 1
        # Add x to root list
        x.left = self.min_node
        x.right = self.min_node.right
        self.min_node.right = x
        x.right.left = x
        x.parent = None
        x.mark = False

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
    def delete(self, x):
        self.decrease_key(x, float('-inf'))
        self.extract_min()

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
