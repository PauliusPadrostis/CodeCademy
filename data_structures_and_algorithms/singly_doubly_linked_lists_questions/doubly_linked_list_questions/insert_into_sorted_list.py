"""
 Given a node in a doubly linked list, write a function to insert
 a new node into the correct sorted position within the list.
"""
import random


class Node:
    def __init__(self, value, prev_node=None, next_node=None):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_prev_node(self):
        return self.prev_node

    def get_next_node(self):
        return self.next_node

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

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

    def add_to_head(self, new_value):
        new_head = Node(new_value)
        current_head = self.head_node

        if current_head is not None:
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)

        self.head_node = new_head

        if self.tail_node is None:
            self.tail_node = new_head

    def add_to_sorted(self, value):
        # Iterate through the list
        current_node = self.get_head_node()
        while current_node:
            # Find where value is more than current node but less than next node
            if current_node.get_value() < value:
                current_node = current_node.get_next_node()
            elif current_node.get_value() >= value:
                # Insert the value
                new_node = Node(value)
                # UPDATING NODES
                if current_node is self.head_node:
                    self.add_to_head(new_node)
                else:
                    current_node.get_prev_node().set_next_node(new_node)
                new_node.set_next_node(current_node)
                new_node.set_prev_node(current_node.get_prev_node())
                current_node.set_prev_node(new_node)
                return


dll = DoublyLinkedList()
values = []
for x in range(10, 0, -1):
    values.append(random.randint(1, 50))
sorted_values = sorted(values)

for y in sorted_values[::-1]:
    dll.add_to_head(y)

print(dll.stringify_list())
dll.add_to_sorted(25)
print(dll.stringify_list())
