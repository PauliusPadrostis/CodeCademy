"""
Given the head of a singly linked list and a value x,
partition it such that all nodes with value less than x come before nodes with value greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
"""
import random



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
    def __init__(self):
        self.head_node = None

    def insert_node(self, new_value):
        new_node = Node(new_value)
        if self.head_node is None:
            self.head_node = new_node
        else:
            last_node = self.head_node
            while last_node.get_next_node() is not None:
                last_node = last_node.get_next_node()
            last_node.set_next_node(new_node)

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


    def merge_lists(self, list1, list2):
        list3 = SinglyLinkedList()

        # Copy nodes of first list to list3
        current_node = list1.get_head_node()
        while current_node:
            list3.insert_node(current_node.get_value())
            current_node = current_node.get_next_node()

        # Copy nodes of second list to list3
        current_node = list2.get_head_node()
        while current_node:
            list3.insert_node(current_node.get_value())
            current_node = current_node.get_next_node()

        return list3

    def reorder_by_n(self, n):
        current_node = self.get_head_node()
        prev_node = None

        less_than_n = SinglyLinkedList()
        greater_than_equal_n = SinglyLinkedList()

        while current_node is not None:
            if current_node.get_value() < n:
                less_than_n.insert_node(current_node.get_value())
            else:
                greater_than_equal_n.insert_node(current_node.get_value())
            current_node = current_node.get_next_node()
        return self.merge_lists(less_than_n, greater_than_equal_n)


ll1 = SinglyLinkedList()
for _ in range(10):
    random_value = random.randint(1, 20)
    ll1.insert_node(random_value)

print(ll1.stringify_list())
print(ll1.reorder_by_n(10).stringify_list())
