import turtle

# Create a screen
screen = turtle.Screen()

# Register the custom image file as a new shape in the Turtle graphics library
screen.register_shape("LOGO.png")  # Replace "custom_logo.gif" with your image file

# Create a Turtle
t = turtle.Turtle()

# Set the shape of the Turtle to the newly registered shape
t.shape("LOGO.png")

# Example usage: Draw a square
for _ in range(4):
    t.forward(100)
    t.right(90)

# Keep the window open until it's closed by the user
turtle.done()