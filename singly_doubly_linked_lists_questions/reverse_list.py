"""
Reverse a Singly Linked List: Write a function to reverse a singly linked list.
Your function should take in the head of the list and return the new head after reversal.
"""


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node


class SinglyLinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def insert_node(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

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

    def reverse_list(self):
        prev_node = None
        current_node = self.head_node
        while current_node is not None:
            next_node = current_node.get_next_node()
            current_node.set_next_node(prev_node)
            prev_node = current_node
            current_node = next_node
        self.head_node = prev_node


ll = SinglyLinkedList()
ll.insert_node(5)
ll.insert_node(4)
ll.insert_node(3)
ll.insert_node(2)
ll.insert_node(1)
print(ll.stringify_list())
ll.reverse_list()
print(ll.stringify_list())
