"""
Reverse the order of elements in a queue using only queue operations
(enqueue, dequeue, and checking if the queue is empty).

Given a queue of integers, reverse its elements using only basic queue operations.
You should not use any additional data structures to hold the elements.
The idea is to understand how to manipulate the order of elements solely with queue operations.

* Initialize a queue with the elements [1, 2, 3, 4, 5]
* Apply the reversing process
* Dequeue all elements from the reversed queue and print them

Expected output:
5
4
3
2
1
"""


class Node:
    def __init__(self, value, prev_node=None, next_node=None):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_prev_node(self):
        return self.prev_node

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def has_space(self):
        return self.max_size is None

    def peek(self):
        if self.size > 0:
            return self.head.get_value()
        else:
            print('Nothing in the queue!')

    def enqueue(self, elem_to_add):
        if self.has_space():
            item = Node(elem_to_add)
            if self.is_empty():
                self.head = item
                self.tail = item
            else:
                self.tail.set_next_node(item)
                self.tail = item
            self.size += 1
        else:
            print('Sorry, no more room!')

    def dequeue(self):
        if self.get_size() > 0:
            elem_to_remove = self.head
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return elem_to_remove.get_value()
        else:
            print('Queue is empty!')

    def reverse_queue(self):
        if self.is_empty():
            return
        data = self.dequeue()
        self.reverse_queue()
        self.enqueue(data)


queue = Queue()
for x in range(1, 6):
    queue.enqueue(x)

queue.reverse_queue()

while not queue.is_empty():
    print(queue.dequeue())