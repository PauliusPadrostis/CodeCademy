"""
Detect a Cycle in a List: Implement an algorithm to determine if a singly linked list has a cycle.
A list has a cycle if some node in the list can be reached again by continuously following the next pointer.
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

    def detect_cycle(self):
        nodes = {}
        current_node = self.head_node
        while current_node:
            # we have to check if the value of the node and the pointer are in the dictionary as a key:value pair
            if (current_node, current_node.get_value()) in nodes.items():
                # if they are, we return True, since that means that we have a cycle
                print("There is a cycle")
                return True
            # if they are not, we assign the nodes pointer as a key and the nodes value as the value
            else:
                nodes[current_node] = current_node.get_value()
            current_node = current_node.get_next_node()
        print('There is no cycle')
        return False


ll = SinglyLinkedList()
ll.insert_node(5)
ll.insert_node(4)
ll.insert_node(3)
ll.insert_node(2)
ll.insert_node(1)

# Keep a reference to the node with value 1
node1 = ll.get_head_node()

# Keep a reference to the last node (with value 5)
last_node = ll.get_head_node()
while last_node.get_next_node() is not None:
    last_node = last_node.get_next_node()

# Create a cycle from the last node to the node with value 3
last_node.set_next_node(node1)

ll.detect_cycle()
