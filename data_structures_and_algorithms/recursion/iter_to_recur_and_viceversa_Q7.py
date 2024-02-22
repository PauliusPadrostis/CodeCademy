"""
Binary trees, trees which have at most two children per node, are a useful
data structure for organizing hierarchical data.

It’s helpful to know the depth of a tree, or how many levels make up the tree.

Implement your version of depth() which has the same functionality using recursive calls!

def depth(tree):
  result = 0
  queue = [tree]

  while queue:
    level_count = len(queue)
    for child_count in range(0, level_count):
      child = queue.pop(0)

      if child["left_child"]:
        queue.append(child["left_child"])
      if child["right_child"]:
        queue.append(child["right_child"])

    result += 1
  return result
"""


def depth(tree_node):
    if tree_node is None:
        return 0

    left_depth = depth(tree_node['left_child'])
    right_depth = depth(tree_node['right_child'])

    if left_depth > right_depth:
        return left_depth + 1
    else:
        return right_depth + 1


# HELPER FUNCTION TO BUILD TREES
def build_bst(my_list):
    if len(my_list) == 0:
        return None

    mid_idx = len(my_list) // 2
    mid_val = my_list[mid_idx]

    tree_node = {"data": mid_val, "left_child": build_bst(my_list[: mid_idx]),
                 "right_child": build_bst(my_list[mid_idx + 1:])}

    return tree_node


# HELPER VARIABLES
tree_level_1 = build_bst([1])
tree_level_2 = build_bst([1, 2, 3])
tree_level_4 = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

# test cases
print(depth(tree_level_1) == 1)
print(depth(tree_level_2) == 2)
print(depth(tree_level_4) == 4)
