# from fibonacci_heap.fibonacci_heap import FibonacciHeap

# def main():
#     heap = FibonacciHeap()
#     # Example of inserting elements
#     heap.insert(10)
#     heap.insert(5)
#     heap.insert(20)

#     # Print the minimum element
#     print("Min:", heap.find_min().key)

#     # Extract the minimum element
#     heap.extract_min()
#     print("New Min:", heap.find_min().key)

# if __name__ == "__main__":
#     main()

from fibonacci_heap.fibonacci_heap import FibonacciHeap

def main():
    heap = FibonacciHeap()

    def display_menu():
        print("\nManaging Heap:")
        print("1. Insert keys (array input)")
        print("2. Find minimum")
        print("3. Extract minimum")
        print("4. Decrease key")
        print("5. Delete key")
        print("6. Display all nodes")
        print("7. Exit")
        print("Enter your choice:")

    def display_heap(self):
        """Display the Fibonacci Heap structure with enhanced details."""
        def traverse(node, indent=0):
            """Recursively traverse and display the heap structure."""
            if not node:
                return
            start = node
            while True:
                prefix = " " * indent
                label = "(min)" if node == self.min_node else ""
                mark = "*" if getattr(node, "mark", False) else ""
                degree = f"[Degree: {node.degree}]"
                print(f"{prefix}{node.key} {label} {mark} {degree}")
                if node.child:
                    print(f"{prefix}  Children of {node.key}:")
                    traverse(node.child, indent + 4)
                node = node.right
                if node == start:
                    break

        if not self.min_node:
            print("Heap is empty.")
        else:
            print("\nRoot List:")
            traverse(self.min_node)

        # Display heap statistics
        print("\nHeap Statistics:")
        print(f"Total nodes: {self.node_count}")
        print(f"Minimum key: {self.min_node.key if self.min_node else 'None'}")
        print(f"Number of roots: {len([node for node in self._iterate_root_list()])}")
        print(f"Marked nodes: {sum(1 for node in self.node_map.values() if node.mark)}")








    while True:
        display_menu()
        try:
            choice = int(input())
            if choice == 1:
             try:
                keys = input("Enter keys to insert (comma-separated): ").split(",")
                keys = [int(k.strip()) for k in keys]
                for key in keys:
                    heap.insert(key)
                print(f"Keys {keys} inserted.")
             except ValueError as e:
                print(e)
            elif choice == 2:
                min_node = heap.find_min()
                print(f"Minimum key: {min_node.key}" if min_node else "Heap is empty.")
            elif choice == 3:
                min_node = heap.extract_min()
                print(f"Extracted minimum key: {min_node.key}" if min_node else "Heap is empty.")
            elif choice == 4:
                try:
                    old_key = int(input("Enter the key to decrease: "))
                    new_key = int(input(f"Enter the new key (less than {old_key}): "))
                    heap.decrease_key(old_key, new_key)
                    print(f"Key {old_key} decreased to {new_key}.")
                except ValueError as e:
                    print(e)
            elif choice == 5:
                key = int(input("Enter the key to delete: "))
                heap.delete(key)
                print(f"Key {key} deleted.")
            elif choice == 6:
                display_heap(heap)
            elif choice == 7:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
