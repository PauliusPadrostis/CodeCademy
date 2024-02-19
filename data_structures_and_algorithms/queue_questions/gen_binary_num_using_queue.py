"""
Use a queue to generate the first N binary numbers starting from 1.

Binary numbers are representations of values using 0s and 1s. Using a queue, generate and print the first N binary
numbers in ascending order. This exercise will help you understand how to use queues for level-order traversal
or breadth-first search (BFS) like operations, which are common in tree and graph algorithms.

* Let N = 5
* Initialize an empty queue and start by enqueueing 1.
* Generate the next binary numbers

Expected output:
1
10
11
100
101
"""

from queue import Queue


def get_binary(n):
    q = Queue()
    q.put('1')

    for _ in range(n):
        d = q.get()
        print(d)

        q.put(d + '0')
        q.put(d + '1')



get_binary(5)