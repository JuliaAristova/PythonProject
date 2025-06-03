def main():
    print_column(3)
    print_row(5)
    print_square(4)

    print_shape(7, 5)

def print_column(height):
    print("#\n" * height, end="")

def print_row(width):
    print("?" * width)

def print_square(size):
    for i in range (size):
       print("*" * size)
    '''
    for i in range (size):
        for j in range(size):
            print ("*", end=" ")
        print()
    '''
def print_shape(width, hight):
    for _ in range (hight):
        print_row(width)

main()