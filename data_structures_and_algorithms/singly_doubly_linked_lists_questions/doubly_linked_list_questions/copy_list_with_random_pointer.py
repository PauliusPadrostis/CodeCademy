"""
Given a doubly linked list where instead of a previous pointer,
each node contains a pointer to another node in the list called random, which could be null.
Write a function that returns a deep copy of the list.
"""
import random


class Node:
    def __init__(self, value, random_node=None, next_node=None):
        self.value = value
        self.random_node = random_node
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_random_node(self):
        return self.random_node

    def get_next_node(self):
        return self.next_node

    def set_random_node(self, random_node):
        self.random_node = random_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None
        self.all_nodes = {}

    def get_head_node(self):
        return self.head_node

    def stringify_list(self):
        string_list = ''
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + '\n'
            current_node = current_node.get_next_node()
        return string_list

    def add_to_head(self, new_value, next_pointer=None, random_pointer=None):
        new_head = Node(value=new_value, random_node=random_pointer, next_node=next_pointer)
        if self.head_node is not None:
            new_head.set_next_node(self.head_node)
        self.head_node = new_head

        if self.tail_node is None:
            self.tail_node = new_head

    def add_to_head_funky(self, new_value):
        new_head = Node(new_value)
        self.all_nodes[new_head] = new_head.get_value()
        current_head = self.head_node

        if current_head is not None:
            new_head.set_next_node(current_head) # Sets new heads next pointer
            flipper = True
            rand = random.randint(0, 5)

            if rand == 5:
                flipper = False

            if flipper:
                new_head.set_random_node(random.choice(list(self.all_nodes.keys())))
            else:
                new_head.set_random_node(None)
        self.head_node = new_head

        if self.tail_node is None:
            self.tail_node = new_head

    def return_copy(self):
        ll2 = DoublyLinkedList()
        node_mapping = {}

        current_node = self.get_head_node()
        while current_node:
            new_node = Node(current_node.get_value())
            node_mapping[current_node] = new_node
            ll2.add_to_head((new_node.get_value()))
            current_node = current_node.get_next_node()

        current_node = self.get_head_node()
        while current_node:
            new_node = node_mapping[current_node]
            new_node.set_next_node(node_mapping.get(current_node.get_next_node()))
            new_node.set_random_node(node_mapping.get(current_node.get_random_node()))
            current_node = current_node.get_next_node()

        return ll2.stringify_list()





dll = DoublyLinkedList()
for x in range(75, 0, -1):
    dll.add_to_head_funky(x)

print(dll.stringify_list())
print(dll.return_copy())