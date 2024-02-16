"""
Write a function that returns all pairs of nodes in a doubly linked list that sum up to a given target.
Each pair should be represented as a list of two node values.
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

    def find_sum_pairs(self, sum):
        p1 = self.get_head_node()
        p2 = self.get_head_node()
        sum_values = []

        # we run the loop till p2 is none
        while p2:
            if p1 is None:
                return sum_values
            if p1.get_next_node() is None:
                p2 = p2.get_next_node()
                p1 = p2.get_next_node()
            if p2.get_next_node() is None:
                return sum_values
            if (p1.get_value() + p2.get_value()) == sum:
                sum_values.append([p1.get_value(), p2.get_value()])
                p1 = p1.get_next_node()
            else:
                p1 = p1.get_next_node()
        return sum_values


dll = DoublyLinkedList()
for x in range(75, 0, -1):
    dll.add_to_head(x)

print(dll.stringify_list())
print(dll.find_sum_pairs(43))