"""
Remove Nth Node From End of List: Given the head of a singly linked list and an integer n,
remove the n-th node from the end of the list and return its head.
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


    def remove_nth(self, n):
        last_pointer = None
        prev_node = None
        first_pointer = self.get_head_node()
        count = 1

        while first_pointer is not None:
            first_pointer = first_pointer.get_next_node()
            count += 1
            if count >= n + 1:
                if last_pointer is None:
                    last_pointer = self.get_head_node()
                else:
                    last_pointer = last_pointer.get_next_node()
                    if last_pointer != self.get_head_node():
                        if prev_node is None:
                            prev_node = self.get_head_node()
                        else:
                            prev_node = prev_node.get_next_node()

                        if last_pointer.get_value() == n + 1:
                            prev_node.set_next_node(last_pointer.get_next_node())
                            last_pointer.set_next_node(None)
                            break
        return


ll1 = SinglyLinkedList()
for x in range(1, 11):
    ll1.insert_node(x)
print(ll1.stringify_list())

ll1.remove_nth(5)

print(ll1.stringify_list())