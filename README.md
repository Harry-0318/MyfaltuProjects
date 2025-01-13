Dynamic Memory Allocation in C++
================================

Dynamic memory allocation is a technique used to allocate memory at runtime, rather than at compile-time. This allows for more flexibility and efficiency in programming.

Why Dynamic Memory Allocation?
-------------------------------

In static memory allocation, the amount of memory allocated at compile-time is fixed. However, this can lead to wasted memory if not all the variables are initialized. With dynamic memory allocation, 
memory is allocated as needed, reducing the likelihood of waste.

How Dynamic Memory Allocation Works
--------------------------------------

Dynamic memory allocation involves using a data structure called a heap. The heap is a region of memory where new blocks of memory are allocated.

Here's an overview of how dynamic memory allocation works:

1.  **Heap Initialization**: When the program starts, the operating system allocates a block of memory for the heap.
2.  **Memory Allocation Request**: When the program needs to allocate memory, it sends a request to the operating system's operating system memory manager (e.g., `malloc`).
3.  **Memory Block Search**: The memory manager searches the heap for an available block of memory that meets the requested size.
4.  **Block Allocation**: If an available block is found, the memory manager allocates it to the requesting process.
5.  **Memory Deallocation**: When a process no longer needs a block of memory, it sends a request to the memory manager to deallocate the memory.

C++ Implementation
-----------------

In C++, dynamic memory allocation is typically achieved using the `new` and `delete` operators.

### Allocating Memory with new

```cpp
int* ptr = new int;  // Allocate an integer on the heap
```

Here, `ptr` is a pointer that points to an integer variable stored in memory. The size of the allocated block is equal to the size of an integer object (`sizeof(int)`).

### Deallocating Memory with delete

```cpp
delete ptr;          // Deallocate the memory and free the pointer
```

Here, `ptr` becomes invalid after it's deallocated.

Example Use Case
-----------------

```cpp
#include <iostream>

int main() {
    int* arr = new int[5];  // Allocate an array of integers on the heap

    for (int i = 0; i < 5; ++i) {
        arr[i] = i * 2;
    }

    std::cout << "Array values:" << std::endl;
    for (int i = 0; i < 5; ++i) {
        std::cout << arr[i] << std::endl;
    }

    delete[] arr;          // Deallocate the memory and free the pointer

    return 0;
}
```

In this example, we allocate an array of integers on the heap using `new`. We then assign values to each element in the array. Finally, we deallocate the memory using `delete[]` after we're done using 
it.

Best Practices
--------------

Here are some best practices for dynamic memory allocation in C++:

*   Always check the return value of `new` to ensure that the allocation was successful.
*   Use smart pointers (like `unique_ptr` and `shared_ptr`) instead of raw pointers where possible, as they help manage memory safety.
*   Avoid using bare `delete` or `new`. Instead, use smart pointers or containers that manage memory automatically.

