# Exercise 2 - implement an efficient queue

A queue is a very common data structure, where the first item to enter the structure is the first one to come out. If we don't think too carefully about how to achieve this, we might be tempted to append to the end of, and shift (pop from the front of), a Python list. We will talk about why this isn't so efficient, and what some better alternatives are.


## Primary exercise

Our primary objective will be to implement a queue data structure that has good performance and memory usage characteristics. The current implementation in queue.py does not! You can use simulation.py to get a sense of how your queue may actually be used in practice.


## Stretch goals

* If you used a double-ended queue approach, take a look at the `collections.deque` implementation and see what similarities there are to your own approach
* If you took a ring buffer approach, does your code work in a multithreaded context?
* If all you were queuing were integers (such as task ids) how might you make your queue more efficient?
