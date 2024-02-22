"""
Recreate the given algorithm using the alternative strategy.
If the example is recursive, write the algorithm using iteration.
If the algorithm uses iteration, solve the problem using recursion.

Start with a classic recursive example, factorial().
This function returns the product of every number from 1 to the given input.

def factorial(n):
  result = 1
  while n != 0:
    result = n * result
    n -= 1
    print(result)
  return result
"""


def factorial(n):
    result = 1

    while n != 0:
        result = n * result
        n -= 1

    return result


# test cases
print(factorial(3) == 6)
print(factorial(0) == 1)
print(factorial(5) == 120)
