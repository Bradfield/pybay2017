# Exercise 4 - parse a raw packet

Now that we're comfortable working with binary data, we can explore an interesting field of computer science that web developers touch every day without realizing it: computer networking.

In this exercise, we've captured a packet that we sent to a server that hosts the pybay website. We'll be exploring that packet to get an understanding of the network protocols involved.


## Main exercise

Given the complexity of the various network protocols, we'll aim to do this exercise together. But if we run out of time and you're doing this at home, or if you just prefer to work on the exercise solo, the overall objective is to understand the meaning of every byte of the captured packet. You can do this by printing and annotating the hexdump, or by copying the hexdump somewhere and writing notes, or simply by asking yourself questions. But ultimately, you should be able to answer questions like:

* Which parts of the data correspond to the ethernet frame, IP packet, TCP segment and HTTP request?
* What version of IP is being used?
* What are the source and destination MAC and IP addresses, and ports?
* What is the TTL on the request and what does that mean?
* Where are the checksums and what do they mean? Can you verify that they are correct?
* ... and so on.


## Stretch goal

Write a program to parse a packet like this and provide a user-friend interface to answering questions like the above.
