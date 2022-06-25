# Stacks and Queues
- A	stack	is	a	collection	of	objects	that	are	added	and	removed	in	”last	in,	first	out”	or	“LIFO”	order.	
- A	queue	is	kind	of	like	the	opposite	of	a	stack.	Instead	of	having	a	“last-in,	first-out”	structure,	it	is	“firstin,	first-out”.

## Challenge
I've created a Stack and Queue Classes for creation, with the related methods for each class.
Also, the unit tests are there with almost 100% coverage

## Approach & Efficiency
I've used the methods approach to make the code more efficient and reusable since creating a methods for executing the program and testing
will be computationally cheaper and will create a much cleaner (readable) code as well.
The Big O notation is **O(1)** time and space performance

## API
- The created methods for Stack class:
1. Push() -> Nodes or items that are put into the stack are pushed
2. Pop() -> Nodes or items that are removed from the stack are popped. When you attempt to pop an empty stack an exception will be raised.
3. Peek() -> View the value of the top Node in the stack. When you attempt to peek an empty stack an exception will be raised.
4. __Str__() -> Convert the elements to string, for viewing the output of the stack
5. isEmpty() ->  Returns true when stack is empty otherwise returns false

- The created methods for Stack for Queue class:
1. Enqueue() -> Nodes or items that are added to the queue.
2. Dequeue() -> Nodes or items that are removed from the queue. If called when the queue is empty an exception will be raised.
3. Peek() -> View the value of the front Node in the queue. If called when the queue is empty an exception will be raised.
4. __Str__() -> Convert the elements to string, for viewing the output of the queue
5. isEmpty() -> Returns true when queue is empty otherwise returns false