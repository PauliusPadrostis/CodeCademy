"""
Towers of Hanoi is an ancient mathematical puzzle that starts off with three stacks and many disks.

The objective of the game is to move the stack of disks from the leftmost stack to the rightmost stack.

The game follows three rules:

    1) Only one disk can be moved at a time.
    2) Each move consists of taking the upper disk
    from one of the stacks and placing it on top of another stack or on an empty rod.
    3) No disk may be placed on top of a smaller disk.

Create a console version of the game. Display data about the game (such as amount of moves it took to finish,
optimal number of moves). Display disk positions after each move to make it easier to orient what disks each
stack has at any given point.
"""

from stack import Stack

print("\nLet's play Towers of Hanoi!!")

# Create the Stacks
stacks = []
left_stack = Stack('Left')
middle_stack = Stack('Middle')
right_stack = Stack('Right')
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

# Set up the Game
num_disks = int(input('\nHow many disks do you want to play with?\n'))
while num_disks < 3:
    num_disks = int(input('Enter a number greater than or equal to 3\n'))

for x in range(num_disks, 0, -1):
    left_stack.push(x)

num_optimal_moves = (2 ** num_disks) - 1
print(f'\nThe fastest you can solve this game is in {num_optimal_moves} moves')


# Get User Input
def get_input():
    choices = [stack.get_name()[0] for stack in stacks]
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print(f'Enter {letter} for {name}')

        user_input = input('')
        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]
        else:
            print('\nThat is not a valid choice\n')


# Play the Game
num_user_moves = 0

while right_stack.get_size() != num_disks:
    print('\n\n\n...Current Stacks...')

    for stack in stacks:
        stack.print_items()

    while True:
        print('\nWhich stack do you want to move from?\n')
        from_stack = get_input()
        print('\nWhich stack do you want to move to?\n')
        to_stack = get_input()
        if from_stack.get_size() == 0:
            print('\n\nThis stack is empty. Try again!')
        elif to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:
            print('\n\nYou can not move to this. Try again!')

print(f'\n\nYou completed the game in {num_user_moves} moves! The optimal number of moves was {num_optimal_moves}!')
if num_user_moves > num_optimal_moves:
    print('\n\nTry again and see if you can improve your score!')
else:
    print('You are really good at this! Try again with more disks!')
