# Exercise 5 - write a Python bytecode interpreter

This exercise is certainly impossible to complete in the time we have available, but it's a good excuse to start talking about compilers and interpreters, including the CPython implementation of the Python language. There are actually 9 exercises in total here, so it should be easy for you to finish some today and some at home.


## Instructions

An asteroid has hit the earth! 🌏☄️ Oh no! All of the Python interpreters and .py files have been destroyed in the fire! 🔥 Somehow, the .pyc files remain unharmed. 🚒👨‍🚒 Your job is to write an interpreter to read and evaluate the surviving .pyc files, so that we can start rebuilding our tragically damaged civilization.

For each of the .pyc files in this directory, read the contents of a file, try to make sense of the bytecode instructions, and slowly build up your interpreter to support the new opcodes.

If you’re not sure where or how to start, "interpreter.py" has a skeleton, and solves the first problem.

The version of Python used is 2.7.10, which is the default Python on most OS X versions. It will help you *a whole bunch* to refer to a couple of key files in the CPython (reference) implementation of Python: [opcode.h](https://github.com/python/cpython/blob/2.7/Include/opcode.h) and [ceval.c](https://github.com/python/cpython/blob/2.7/Python/ceval.c). You may even spend most of your time reading ceval.c! This is a kind of victory state, too.

Another useful resource is the [`dis`](https://docs.python.org/2/library/dis.html), both for its functionality and its documentation.

Hopefully this exercise will raise a bunch of questions and start some interesting conversations! Please don’t hesitate to ask me about them. 🙂


## More resources

Allison Kaptur has a couple of closely related resources: a book chapter in *500 Lines or Less* called [A Python Interpreter Written in Python](http://aosabook.org/en/500L/a-python-interpreter-written-in-python.html) and a talk from PyCon 2015 called [Bytes in the Machine](https://www.youtube.com/watch?v=HVUTjQzESeo). These are both great places to start if you want to revise what we covered or revisit from a different angle.

An excellent more advanced resource is the videos from a short course by Philip Guo (pgbovine) on [CPython internals](http://pgbovine.net/cpython-internals.htm). Watching and understanding these will make you a much more effective Python user.
