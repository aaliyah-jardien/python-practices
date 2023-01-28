

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    while True:
        shape_param = input("Which shape would you like to draw?\n(Pyramid, Sqaure, Triangle): ").lower()

        if shape_param == "pyramid":
            return draw_pyramid()
        elif shape_param == "sqaure":
            return draw_square()
        elif shape_param == "triangle":
            return draw_triangle()
        else:
            print("Please enter a valid shape.")
        # return shape_param


# TODO: Step 1 - get height (it must be int!)
def get_height():

    height = int(input("Enter shape height: "))

    return height


# TODO: Step 2
def draw_pyramid(height, outline):  # parameters, where the values are being passed through

    for x in range(height):
        for y in range(height - x):
            print(" ", end=" ")     # prints empty triangle
        for z in range(x):
            print("*", end=" ")
        for a in range(x + 1):
            print("*", end=" ")
        print()

    print('pyramid')


# TODO: Step 3
def draw_square(height, outline):
    print('square')


# TODO: Step 4
def draw_triangle(height, outline):
    print('triangle')


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    draw_pyramid(height, outline)


# TODO: Step 5 - get input fheight_paramrom user to draw outline or solid
def get_outline():
    return False


if __name__ == "__main__":
    shape_param = get_shape()   # variable of function
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

