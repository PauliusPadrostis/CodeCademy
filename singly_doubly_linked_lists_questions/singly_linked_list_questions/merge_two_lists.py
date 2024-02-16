"""
Merge Two Sorted Lists: Given two singly linked lists that are sorted in ascending order,
merge them into a single sorted linked list and return it.
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

    @staticmethod
    def merge_lists(list1, list2):
        list3 = SinglyLinkedList()

        current_head_l1 = list1.get_head_node()
        current_head_l2 = list2.get_head_node()

        while current_head_l2 and current_head_l1:
            list3.insert_node(current_head_l1.get_value())
            list3.insert_node(current_head_l2.get_value())

            current_head_l1 = current_head_l1.get_next_node()
            current_head_l2 = current_head_l2.get_next_node()

        return list3


# list 1
ll1 = SinglyLinkedList()
ll1.insert_node(5)
ll1.insert_node(4)
ll1.insert_node(3)
ll1.insert_node(2)
ll1.insert_node(1)

# list 2
ll2 = SinglyLinkedList()
ll2.insert_node(5)
ll2.insert_node(4)
ll2.insert_node(3)
ll2.insert_node(2)
ll2.insert_node(1)

print(SinglyLinkedList.merge_lists(ll1, ll2).stringify_list())
print(SinglyLinkedList.merge_lists(ll1, ll2))
