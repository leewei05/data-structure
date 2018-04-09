## Binary Trees

### Trees

* data and connections between the nodes
* root node: all the other nodes can be access via the root node
* there must only be a **single path** from the root node to other nodes
* leaf node: with no child

### Binary Search Trees

* BST are data structures 
* every node can have at most two children (left and right)
* left child: smaller than parent
* right child: greater than parent
* height of the tree: the number of layers it has
	* we should keep the height of the tree at the minimum ( h = O(logN) )
	* if the tree is unbalanced: the h = O(logN) relation will no longer be valid and the operation's running time is no more logarithmic

**Why is it good?**

* Because we get rid of half of the data in which we are searching
* O(logN) on average on operation but it is O(N) if the tree is not balanced

* Delete a node
    1. a leaf node -> set it to null
    2. a node with one child -> set the parent node to the child node
    3. a node with two children -> 
         1. find the largest number(predecessor) at the left subtree, and swap the predecessor with the node 
         2. find the smallest number(successor) at the right subtree, and swap the successor with the node

* Traversal: visit every node in the tree
     1. In-order traversal -> left + root node + right
     2. Pre-order traversal -> root node + left + right
     3. Post-order traversal -> left + right + root node

### AVL Trees

AVL Trees guaranteed the tree is balanced (**O(logN)**)

* The insertion operation is the same but we need to check whether the tree is unbalanced or not
* Height of a node: length of the longest path from it to a leaf
* AVL Trees requires the height of left and right child of every node to differ at most +1 or -1 

` |height(leftSubtree) - height(rightSubtree) | <= 1`

* rotations: to the left or the right, the in-order traversal is the same 

