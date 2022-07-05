# Trees
<!-- Short summary or background information -->
A trees are widely used abstract data type that represents a hierarchical
tree structure with a set of connected nodes. Each node in the tree can be connected to
many children, but must be connected to exactly one parent, except for the root node, which has no parent.

## Challenge
<!-- Description of the challenge -->


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
I used the recursion in building all the methods, the Big O for each as the following:

##### For pre_order(), in_order() and post_order():

- Time: O(n)
- Space: O(n)
##### For add() and contains():

- Time: O(log n)
- Space: O(1)

## API
<!-- Description of each method publicly available in each of your trees -->
1. BinaryTree class have the following methods:

- pre_order(): returns the nodes in the order: root >> left >> right
- in_order(): returns the nodes in the order: left >> root >> right
- post_order(): returns the nodes in the order: left >> right >> root



2.  BinarySearchTree have the following methods:

- add(): adds a node in the right place in the binary search tree, if less than root the node goes to the left, and if more it goes to the right
- contains(): returns True if the value found and False if not.