# Exercise 3 - implement a dictionary

We're very lucky to have a well-implemented hashmap type in Python, called `dict`. But a great way to figure out how it actually works (so, how best to use it) we're going to pretend that it doesn't exist, then re-implement it! There are many different ways to do this, so we'll talk through some simpler and more advanced ways to do it.


## Primary exercise

Implement a dictionary in "dictionary.py" and write tests for it in "test.py". The given implementation is not great! It doesn't handle updates for instance, and slows down as we add more items.

The easier version of this exercise is to fix and extend the current approach, of using a list of key-value pairs.

The harder version is to implement something with logarithmic or constant time lookup characteristics, like a treemap or hashmap. A hashmap becomes more complicated when handling collisions, so you may wish to assume collisions won't happen, at least as a first milestone.


## Stretch goals

* If you completed the easier version of the exercise, try the harder one!
* If you aren't handling collisions yet, try doing so.
* If you are handling collisions with chaining, try open addressing instead.
* If we knew the types of the values, how might we change the implementation?
* Read the implementation of `dict` in Python, and consider what exists in the full implementation that wasn't in yours.
