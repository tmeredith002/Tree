import math

GREEN = "\033[32m"
RED = "\033[31m"
BLUE = "\033[34m"
YELLOW = "\033[33m"
RESET = "\033[0m"
BLACK_BG = "\033[40m"
BROWN = "\033[38;5;94m"

def _print_tree(height, step, left_color="red", right_color="blue"):
    if step > height: return
    #Left Side
    if step % 2 == 0 and left_color == "red": #Blue
        print(BLACK_BG + (' ' * (height - step - 1)) \
             + BLUE + '@' + GREEN + (('*' * (step - 1)) + '*' * step))
        left_color = "blue"
    elif step % 2 == 0 and left_color == "blue": #Red
        print(BLACK_BG + (' ' * (height - step - 1)) \
             + RED + '@' + GREEN + (('*' * (step - 1)) + '*' * step))
        left_color = "red"
    #Right Side
    elif step % 2 != 0 and right_color == "blue": #Red
        print(BLACK_BG + (' ' * (height - step)) \
               + GREEN + ('*' * (step - 1) + ('*' * step)) \
               + RED + '@' + BLACK_BG)
        right_color = "red"
    elif step % 2 != 0 and right_color == "red": #Blue
        print(BLACK_BG + (' ' * (height - step)) \
               + GREEN + ('*' * (step - 1) + ('*' * step)) \
               + BLUE + '@' + BLACK_BG)
        right_color = "blue"
    _print_tree(height, step + 1, left_color, right_color)

def print_tree(height):
    print(BLACK_BG + (' ' * (height - 1)) + YELLOW + '$' + BLACK_BG) #Print star
    print(BLACK_BG + (' ' * (height - 1)) + GREEN + '*' + BLACK_BG) #Print top
    if height <= 0: return
    _print_tree(height, 2) #Recursively print tree starting at step 2
    for _ in range(math.ceil(height / 10)):
        print(BLACK_BG + (' ' * (height - 2)) + BROWN + '[ ]' + BLACK_BG) #Print trunk
    print(RESET)

print_tree(int(input(RESET + 'Enter tree height: ' + BLACK_BG)))
print(RESET)
