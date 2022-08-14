# Challenge Summary
<!-- Description of the challenge -->
By Using Hashmap implementation as a part of your algorithm, a set of values found in both trees are returned.

## Whiteboard Process
<!-- Embedded whiteboard image -->
![Tree Intersection Whiteboard](tree_intersection.png)


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
I used the function approach to make the code more efficient and reusable since creating a methods for executing the program and testing
will be computationally cheaper and will create a much cleaner (readable) code as well.

**The Big O notation is:**
- Time --> O(N) 
- Space --> O(N)


## Solution
<!-- Show how to run your code, and examples of it in action -->
1. Create two trees
2. Call tree_intersection() using pre-order or in-order or post-order when passing it to the function
3. The common values will be returned
