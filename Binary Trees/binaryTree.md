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
* O(logN) time complexity
