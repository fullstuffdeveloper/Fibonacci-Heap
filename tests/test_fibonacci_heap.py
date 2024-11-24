import unittest
from fibonacci_heap.node import Node
from fibonacci_heap.fibonacci_heap import FibonacciHeap


class TestFibonacciHeap(unittest.TestCase):
    
    def setUp(self):
        # Initialize a new Fibonacci Heap before each test
        self.heap = FibonacciHeap()

    def test_insert_and_find_min(self):
        # Insert nodes and verify the minimum
        self.heap.insert(10)
        self.heap.insert(5)
        self.heap.insert(20)
        self.assertEqual(self.heap.find_min().key, 5)

    def test_extract_min(self):
        # Insert nodes and extract the minimum
        self.heap.insert(15)
        self.heap.insert(10)
        self.heap.insert(5)
        min_node = self.heap.extract_min()
        self.assertEqual(min_node.key, 5)
        self.assertEqual(self.heap.find_min().key, 10)

    def test_decrease_key(self):
        # Insert nodes and decrease key of one node
        node = self.heap.insert(10)
        self.heap.insert(20)
        self.heap.decrease_key(node, 5)
        self.assertEqual(self.heap.find_min().key, 5)

    def test_delete(self):
        # Insert nodes, delete one node, and check min
        node = self.heap.insert(30)
        self.heap.insert(15)
        self.heap.insert(5)
        self.heap.delete(node)
        self.assertEqual(self.heap.find_min().key, 5)

    def test_merge_heaps(self):
        # Merge two heaps and verify the min node
        heap2 = FibonacciHeap()
        self.heap.insert(10)
        heap2.insert(3)
        self.heap.merge(heap2)
        self.assertEqual(self.heap.find_min().key, 3)

if __name__ == '__main__':
    unittest.main()
