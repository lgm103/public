import turtle

def draw_pyramid(levels):
    turtle.speed(1)
    turtle.penup()
    turtle.goto(-levels * 20, -levels * 20)  # Move to starting position
    turtle.pendown()

    for i in range(levels):
        for j in range(i + 1):
            # Draw a square for each block of the pyramid
            draw_square(turtle.xcor() + j * 40, turtle.ycor() + i * 40)

        # Reset position for the next row
        turtle.penup()
        turtle.goto(-levels * 20 + (i + 1) * 20, -levels * 20 + (i + 1) * 40)
        turtle.pendown()

def draw_square(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    for _ in range(4):
        turtle.forward(40)  # Length of square side
        turtle.right(90)

# Set up the screen
turtle.speed(3)
turtle.title("Pyramid Drawing")
turtle.bgcolor("white")
turtle.color("blue")

# Draw a pyramid with the desired number of levels
num_levels = 5  # You can change this number to make a larger or smaller pyramid
draw_pyramid(num_levels)

# Finish the drawing
turtle.done()
