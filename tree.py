import math
def _print_tree(height, step):
    if step > height: return
    if step % 2 == 0: print(' ' * (height - step - 1) + '@' + ('*' * (step - 1)) + '*' * step)
    else: print(' ' * (height - step) + '*' * (step - 1) + ('*' * step) + '@')
    _print_tree(height, step + 1)

def print_tree(height):
    print(' ' * (height - 1) + '$')
    print(' ' * (height - 1) + '*')
    if height <= 0: return
    _print_tree(height, 2)
    for _ in range(math.ceil(height / 10)):
        print(' ' * (height - 2) + '[ ]')

print_tree(int(input('Enter tree height: ')))
