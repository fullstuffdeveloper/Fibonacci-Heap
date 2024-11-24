# Fibonacci Heap Project

This project is an implementation of a Fibonacci Heap (min-heap) in Python, designed as part of the coursework for COSC 6334.

## Features

- Implementation of **Fibonacci Heap** operations:
  - `Insert`
  - `Extract-Min`
  - `Union`
  - `Decrease-Key`
  - `Delete`
- Provides efficient time complexity for operations, leveraging the Fibonacci Heap's amortized analysis.
- Includes a **unit testing framework** to verify the implementation.
- Accompanied by a **detailed report** and a **presentation** outlining the theoretical and practical aspects of Fibonacci Heaps.

## Project Structure

FIBONACCI_HEAP_PROJECT/
├── fibonacci_heap/
│ ├── **init**.py # Initialization for Fibonacci Heap module
│ ├── fibonacci_heap.py # Core Fibonacci Heap implementation
│ ├── node.py # Implementation of nodes used in the heap
├── tests/
│ ├── **init**.py # Initialization for testing
│ ├── test_fibonacci_heap.py # Unit tests for Fibonacci Heap operations
├── report/
│ ├── report.pdf # Detailed report on Fibonacci Heap
│ ├── presentation.pptx # PowerPoint presentation on the project
├── main.py # Main script to demonstrate heap operations
├── README.md # Documentation file (this file)

## Installation

To run this project, ensure you have Python 3.8+ installed. Then, follow the steps below:

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd FIBONACCI_HEAP_PROJECT
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   _(If you don't have a `requirements.txt`, mention the libraries used, like `pytest` for testing.)_

3. Run the unit tests to verify the implementation:

   ```bash
   pytest tests/
   ```

4. Execute the main script to see the heap in action:
   ```bash
   python main.py
   ```

## Usage

This project demonstrates the functionality of Fibonacci Heaps for educational and practical purposes. Run the `main.py` script to perform operations like insertions, extract-min, and merging.

## Documentation

- **Report**: A comprehensive explanation of Fibonacci Heaps, including their applications and complexity analysis.
- **Presentation**: A visual summary of the project's objectives, implementation, and results.

## Future Enhancements

- Extend the implementation to include **max-heap** variants.
- Optimize memory usage for large-scale applications.
- Add visualization tools to demonstrate heap operations interactively.

## Contributors

- **[Abhishek Jha]** - Implementation and Documentation

## References

- "Introduction to Algorithms" by Cormen, Leiserson, Rivest, and Stein (Fibonacci Heaps chapter)
- Lecture notes and resources from COSC 6334.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

You can customize this further by adding your GitHub repository URL, and if you have additional insights or unique features, include them in the relevant sections. Let me know if you'd like to refine it further!
