"""
Understand and implement the basic operations of a queue, including enqueue (adding items),
dequeue (removing items), and checking if the queue is empty, peek and so on.

* Create a queue
* Enqueue the following numbers in order: 5, 10, 15
* Dequeue an item and print it
* Check if the queue is empty and print the result
* Dequeue all remaining items and print them

Expected output:
5
False
10
15
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


queue = Queue()
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)
print(queue.dequeue())
print(queue.is_empty())
print(queue.dequeue())
print(queue.dequeue())
