import turtle

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.left(90)

def draw_pyramid(base_size, layers):
    t = turtle.Turtle()
    t.speed(1)  # Setting the speed of the turtle

    # Starting position
    t.penup()
    t.goto(-base_size // 2, 0)  # Center the base on the screen
    t.pendown()

    for layer in range(layers):
        size = base_size - (layer * 20)  # Decrease size for each layer
        # Draw the square for each layer
        draw_square(t, size)

        # Move to the next layer
        t.penup()
        t.goto(t.xcor() + 10, t.ycor() + 20)  # Move turtle for the next layer
        t.pendown()

    turtle.done()

# Set the base size and number of layers for the pyramid
base_size = 200
layers = 5

draw_pyramid(base_size, layers)
