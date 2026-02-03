# Fractal Art with Recursion and Turtle Graphics

# Learning Objective:
# This tutorial will teach you how to generate beautiful fractal art
# using the concept of recursion and Python's built-in Turtle graphics module.
# We will focus on understanding how recursive functions break down
# complex problems into smaller, self-similar parts to create intricate patterns.

import turtle # Import the turtle module, which provides tools for drawing graphics.

# --- Configuration ---
# These variables allow you to easily adjust the appearance of your fractal.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PEN_COLOR = "blue" # The color of the lines drawn by the turtle.
BACKGROUND_COLOR = "black" # The background color of the drawing window.
INITIAL_SPEED = 0 # Set to 0 for the fastest drawing speed.
INITIAL_PENSIZE = 1 # The thickness of the lines.

# --- Fractal Generation Function ---

def draw_fractal(turtle_obj, length, depth):
    """
    Recursively draws a fractal pattern.

    Args:
        turtle_obj: The turtle object used for drawing.
        length: The current length of the line segment to draw.
        depth: The current recursion depth, controlling how complex the fractal is.
               When depth reaches 0, the recursion stops.
    """
    # Base Case: This is the stopping condition for our recursion.
    # When depth is 0, we draw a single line segment and stop recursing.
    # This prevents infinite loops and ensures the fractal has a defined structure.
    if depth == 0:
        turtle_obj.forward(length) # Move the turtle forward by the specified length.
        return # Exit the function, stopping this branch of recursion.

    # Recursive Step: If depth is greater than 0, we break down the problem
    # into smaller, self-similar sub-problems.
    # We divide the current 'length' into a fraction (e.g., 1/3) for the next recursive calls.
    # We also decrease the 'depth' by 1 for each recursive call.

    # Calculate the length for the next smaller segments.
    # We use length / 3.0 to ensure floating-point division.
    new_length = length / 3.0

    # First segment: Draw a segment of the new length.
    draw_fractal(turtle_obj, new_length, depth - 1)

    # Turn left and draw the second segment.
    # The angle (90 degrees in this case) determines the shape of the fractal.
    turtle_obj.left(90)
    draw_fractal(turtle_obj, new_length, depth - 1)

    # Turn right twice (effectively 180 degrees from the previous direction)
    # to go back and then turn right for the third segment.
    turtle_obj.right(180)
    draw_fractal(turtle_obj, new_length, depth - 1)

    # Turn left again to return to the original orientation before the last segment.
    turtle_obj.left(90)
    draw_fractal(turtle_obj, new_length, depth - 1)

    # After drawing all segments for this level, we need to backtrack.
    # This is crucial for recursion to build the pattern correctly.
    # We move backwards by the length of the current segment.
    turtle_obj.backward(length)


# --- Setup and Execution ---

def main():
    """
    Sets up the turtle screen and turtle object, and then initiates
    the fractal drawing process.
    """
    # 1. Set up the screen
    screen = turtle.Screen() # Create a graphics window.
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT) # Set the dimensions of the window.
    screen.bgcolor(BACKGROUND_COLOR) # Set the background color of the window.
    screen.title("Recursive Fractal Art") # Set the title of the window.

    # 2. Create a turtle object
    artist = turtle.Turtle() # Create a turtle object, which will be our "pen".
    artist.speed(INITIAL_SPEED) # Set the drawing speed to the fastest.
    artist.color(PEN_COLOR) # Set the color of the pen.
    artist.pensize(INITIAL_PENSIZE) # Set the thickness of the pen.
    artist.penup() # Lift the pen so it doesn't draw while moving to the starting position.

    # 3. Position the turtle to start drawing.
    # We move the turtle to the bottom-left area of the screen
    # to give the fractal room to grow upwards and to the right.
    artist.goto(-SCREEN_WIDTH / 3, -SCREEN_HEIGHT / 2.5)
    artist.pendown() # Put the pen down to start drawing.

    # 4. Define initial parameters for the fractal.
    # 'initial_length' is the length of the largest segments.
    # 'initial_depth' controls the complexity: higher means more detail.
    initial_length = 300
    initial_depth = 4 # Experiment with values from 1 to 5 for different complexity.

    # 5. Call the recursive function to draw the fractal.
    # This is where the magic happens!
    draw_fractal(artist, initial_length, initial_depth)

    # 6. Hide the turtle after drawing.
    artist.hideturtle()

    # 7. Keep the window open until manually closed.
    screen.mainloop()

# --- Example Usage ---
# This block ensures that the 'main()' function is called
# only when the script is executed directly (not when imported as a module).
if __name__ == "__main__":
    main()

# --- How to Experiment ---
# - Change 'initial_depth': Higher numbers create more intricate patterns but take longer to draw.
# - Change 'PEN_COLOR' and 'BACKGROUND_COLOR'.
# - Modify the angles in 'draw_fractal': Changing 'left(90)' and 'right(180)'
#   will create entirely different fractal shapes. For example, try 'left(60)'
#   and 'right(120)' to create Sierpinski triangles.
# - Change the fraction for 'new_length' calculation (e.g., length / 2.0).
#   Be mindful that this can significantly change the fractal's appearance.