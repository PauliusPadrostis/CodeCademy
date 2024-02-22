"""
Implement your version of sum_digits() which has the same functionality using recursive calls!

def sum_digits(n):
  if n < 0:
    ValueError("Inputs 0 or greater only!")
  result = 0
  while n is not 0:
    result += n % 10
    n = n // 10
  return result + n
"""


def sum_digits(n):
    if n <= 9:
        return n
    last_digit = n % 10
    return sum_digits(n // 10) + last_digit


# test cases
print(sum_digits(12) == 3)
print(sum_digits(552) == 12)
print(sum_digits(123456789) == 45)
