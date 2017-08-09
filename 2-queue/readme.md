# Exercise 2 - implement an efficient queue

A queue is a very common data structure, with the behavior that the thing that's been waiting longest in the queue comes out soonest. If you don't think too carefully about how to achieve this, you might find yourself appending to the end of, and popping from the front of, a Python list. We will talk about why this isn't so efficient, and what some better alternatives are.


## Primary exercise

Our primary objective will be to implement a queue data structure that has good performance and memory usage characteristics. The current implementation in queue.py does not! You can use simulation.py to get a sense of how your queue may actually be used in practice.


## Stretch goals

* If you used a double-ended queue approach, take a look at the `collections.deque` implementation and see what similarities there are to your own approach
* If you took a ring buffer approach, does your code work in a multithreaded context?
* If all you were queuing were integers (such as task ids) how might you make your queue more efficient?
