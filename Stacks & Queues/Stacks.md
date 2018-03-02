## Stack

* abstract data type 
* operations: pop(), push(), peek()(Look at the top of the data)
* LIFO structure: last in first out

### Stack memory (managed by the OS)

* A call stack is an abstract data type that stores methods / functions of the computer program
* Release memory after each active subroutine finishes executing
* Stores temporary variables created by each function
* **Local variables** : they are on the stack, after the function returns they are lost

### Heap memory

* Heap is a region of memory that is not managed automatically
* This is a large region of memory
* We have to deallocate these memory chunks, if not: memory leak

### Stack vs Heap

|             Stack memory            |        Heap memory       |
|:-----------------------------------:|:------------------------:|
|           limited in sizes          |      no size limits      |
|             fast access             |        slow access       |
|           local variables           |          objects         |
| space is managed efficiently by CPU | memory may be fragmented |
|     variables cannot be resized     | variables can be resized |

### Stack and recursion(遞迴)

* The recursive function calls are pushed onto the stack until we bump into the base case, if too many function calls: the stack may cause a stack overflow error