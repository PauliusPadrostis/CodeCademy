"""
 Write a function to delete a given node from a doubly linked list.
 You will not be given access to the head of the list, instead, you will be given the node to be deleted directly.
 (Assume that the value that needs deleting doesn't repeat)
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

    def delete_node(self, value):
        # Iterate through the list
        current_node = self.get_head_node()
        while current_node:
            if current_node is not None:
                # Find the node whose values matches value
                if current_node.get_value() != value:
                    current_node = current_node.get_next_node()
                else:
                    # Update nodes
                    if current_node is self.head_node:
                        self.head_node = current_node.get_next_node()
                        current_node.set_next_node(None)
                        self.head_node.set_prev_node(None)
                        return
                    elif current_node is self.tail_node:
                        self.tail_node = current_node.get_prev_node()
                        current_node.set_prev_node(None)
                        self.tail_node.set_next_node(None)
                        return
                    else:
                        prev_node = current_node.get_prev_node()
                        next_node = current_node.get_next_node()
                        prev_node.set_next_node(next_node)
                        next_node.set_prev_node(prev_node)
                        current_node.set_next_node(None)
                        current_node.set_prev_node(None)
                        return


dll = DoublyLinkedList()
for x in range(10, 0, -1):
    dll.add_to_head(x)

print(dll.stringify_list())
dll.delete_node(5)
print(dll.stringify_list())
