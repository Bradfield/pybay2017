#!/usr/bin/env python3

from datetime import datetime, timedelta
from random import random

from queue import Queue


def run_tests():
    """
    A few simple assertions to ensure the queue actually works.

    Add your own!
    """
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.is_empty()
    print('Tests passed')


def run_simulation(length=10):
    """
    Run a simulation where a producer periodically adds to a queue, and
    a consumer periodically pulls from it.
    """
    print('Running simulation for {}s'.format(10))
    start = last_msg = datetime.now()
    delta = timedelta(seconds=10)
    msg_freq = timedelta(seconds=1)
    num_enqueues = 0
    num_dequeues = 0
    max_queue_size = 0
    queue = Queue()
    while True:
        now = datetime.now()
        if now - start > delta:
            break
        if now - last_msg > msg_freq:
            print('{} enqueues, {} dequeues, {} max queue size'
                  .format(num_enqueues, num_dequeues, max_queue_size))
            last_msg = now
        if random() < 0.5:  # 50% chance there's a new message
            queue.enqueue((now, "New message!"))
            num_enqueues += 1
            max_queue_size = max(max_queue_size, queue.size())
        if random() < 0.5:  # 50% chance a message is removed
            if not queue.is_empty():
                queue.dequeue()
                num_dequeues += 1
    ops = (num_enqueues + num_dequeues) / length
    print('Simulation complete, ran {:,} operations per second'.format(ops))


if __name__ == '__main__':
    run_tests()
    run_simulation()
