# Hashtables
<!-- Short summary or background information -->
A hash table uses a hash function to compute an index, also called a hash code,
into an array of buckets or slots, from which the desired value can be found.

## Challenge
<!-- Description of the challenge -->
Implement a Hashtable Class with the following methods:

1. set
  - Arguments: key, value
  - Returns: nothing
  - This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
  - Should a given key already exist, replace its value from the value argument given to this method.
2. get
    - Arguments: key
    - Returns: Value associated with that key in the table
3. contains
    - Arguments: key
    - Returns: Boolean, indicating if the key exists in the table already. 
   
4. keys
    - Returns: Collection of keys
5. hash
    - Arguments: key
    - Returns: Index in the collection for that key


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
I used the function approach to make the code more efficient and reusable since creating a methods for executing the program and testing
will be computationally cheaper and will create a much cleaner (readable) code as well.

**The Big O notation is:**
- Time: O(1)
- Space: O(n)

## API
<!-- Description of each method publicly available in each of your hashtable -->
I've the following methods in Hashtable class:
- set(): to inserts data to the hash table.
- get(): to gets value of the required key with collision handled.
- contains(): returns true or false if the key is in the hashed table or not
- keys(): returns a collection of all the existed keys in the hashed table.