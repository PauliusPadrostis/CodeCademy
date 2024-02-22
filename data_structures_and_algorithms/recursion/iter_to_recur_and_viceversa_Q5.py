"""
Implement your version of is_palindrome() which has the same functionality using recursive calls!

def is_palindrome(my_string):
  string_length = len(my_string)
  middle_index = string_length // 2
  for index in range(0, middle_index):
    opposite_character_index = string_length - index - 1
    if my_string[index] != my_string[opposite_character_index]:
      return False
  return True
"""


def is_palindrome(my_string):
    if len(my_string) < 2:
        return True

    if my_string[0] != my_string[-1]:
        return False

    return is_palindrome(my_string[1:-1])


# test cases
print(is_palindrome("abba") is True)
print(is_palindrome("abcba") is True)
print(is_palindrome("") is True)
print(is_palindrome("abcd") is False)
