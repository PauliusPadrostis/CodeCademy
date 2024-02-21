"""
The language of the flowers has a long history and has often been a topic resigned to the
domain of dusty books in a thrift bookseller or a library. With Blossom, we want to give
people lightning fast access to all the possible meanings of their favorite flowers.

In this project, implement a hash map to relate the names of flowers to their meanings.
In order to avoid collisions when hashing function collides the names of two flowers,
use separate chaining. Implement the Linked List data structure for each of these separate chains.

1) Write a flower array, where the keys are flower names and values are meanings of the flowers.
2) Define a HashMap class with the usual methods for retrieving, assigning, hashing and compressing. Use separate
chaining to avoid collisions.
3) Implement a Linked List data structure to be used as the underlying data structure.
4) Check if everything is working by trying to retrieve some flower meanings by their key.
"""

from linked_list import Node, LinkedList
from blossom_lib import flower_definitions


class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for _ in range(size)]

    def hash(self, key):
        return sum(key.encode())

    def compress(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        payload = Node([key, value])
        list_at_array = self.array[array_index]

        for node in list_at_array:
            if key == node[0]:
                node[1] = value
                return
        list_at_array.insert(payload)

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]

        for node in list_at_index:
            if node[0] == key:
                return node[1]
        return None


blossom = HashMap(len(flower_definitions))

for item in flower_definitions:
    blossom.assign(item[0], item[1])

print(blossom.retrieve('daisy'))
