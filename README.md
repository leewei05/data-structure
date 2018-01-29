# Data Structure in Python

## Arrays 

A collection of values each identified by an index.

* index starts at zero
* random access is possible if you know the index of the item

### Advantages

* random access // O(1) order time complexity 
* fast and easy to implement

### Disadvantages

* it is not so dynamic data structure
* it is not able to store items with different types (C++, JAVA)

-------------

## Linked lists

nodes and references / pointers pointing from one node to the other.

* The last references is pointing to a Null
* each node contains a data and a reference / link

### Advantages

* dynamic data structures
* allocate the needed memory in run-time
* store item in different sizes
* it's easy to grow sizes of the linked lists

### Disadvantages

* waste memory because of the references
* sequential access: nodes must be read from the beginning 
* linked lists are difficult to navigate backwards, solution: doubly linked lists -> easier to read but waste of memory

## Array vs Linked lists

1. Search
    * array list search operation can use random access / O(1) time complexity
    * linked list performance is O(N) time complexity
    * **Solution** Array list is better for search operation

1. Deletion
    * array list removing the first element takes O(N) time, removing the last item takes O(1) time
    * linked list remove operation takes O(1) time if we remove items from the beginning
    * **Solution** Linked list is better for delete operation
    * **Why?** removal only requires change in the pointer location which can be done very fast

1. Memory management
    * **Solution** Array list is better for memory management
    * **Why?** Arrays do not need extra memory, linked lists on the other hand do need extra memory to store the references / pointers 

1. Comparison table
|                     | Linkedlist | Arrays |
|---------------------|------------|--------|
| Search              | O(N)       | O(1)   |
| Insert at the start | O(1)       | O(N)   |
| Insert at the end   | O(N)       | O(1)   |
| Waste space         | O(N)       | 0      |