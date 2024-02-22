"""
Implement your version of find_min() which has the same functionality using recursive calls!

def find_min(my_list):
  min = None
  for element in my_list:
    if not min or (element < min):
      min = element
  return min
"""


def find_min(my_list):
    if len(my_list) == 0:
        return None
    if len(my_list) == 1:
        return my_list[0]

    if my_list[0] < my_list[1]:
        temp = my_list[0]
    else:
        temp = my_list[1]

    my_list[1] = temp
    return find_min(my_list[1:])


# test cases
print(find_min([42, 17, 2, -1, 67]) == -1)
print(find_min([]) is None)
print(find_min([13, 72, 19, 5, 86]) == 5)
