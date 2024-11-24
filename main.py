from fibonacci_heap.fibonacci_heap import FibonacciHeap

def main():
    heap = FibonacciHeap()
    # Example of inserting elements
    heap.insert(10)
    heap.insert(5)
    heap.insert(20)

    # Print the minimum element
    print("Min:", heap.find_min().key)

    # Extract the minimum element
    heap.extract_min()
    print("New Min:", heap.find_min().key)

if __name__ == "__main__":
    main()
