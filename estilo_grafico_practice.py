# Explore the universe of numbers and their squares. Here is the code that plots the relationship between positive integers and their squares, styled as a purple dashed line. Run the code to see it visualizing the squares of numbers!

import matplotlib.pyplot as plt

# Plot for the Math and Squares scenario
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], color='purple', linestyle='--')
plt.xlabel('Positive Integers')
plt.ylabel('Squares')
plt.title('Graph of Squares')
plt.grid(True)
plt.show()

# Let's jazz up your plot! Try enhancing the Fibonacci plot by changing its style. Your task is to modify the color, line style, and marker to make your plot even more snazzy. Aim to represent a 'green' streak of Fibonacci numbers with dots (':') and 'x' marks. Update the plt.plot() function parameters accordingly. Are you ready to control the visual story?

# Plotting Fibonacci sequence as a line plot with style
numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
plt.plot(numbers, color='green', linestyle=':', marker='x', label='Fibonacci')  # updated settings
plt.title('Fibonacci Sequence')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)
plt.legend() # Add a legend for clarity
plt.show()

# Let's get creative, Space Explorer! Update the starter code so that the plot of cubic numbers features a magenta dash-dot line with diamond markers. To make it, pass 'dashdot' as the linestyle and 'D' as the marker.

# These elements help us visually distinguish between different data sets in a plot. Now is the time to apply your newfound skills in styling plots with Matplotlib!

# Number sequences: x values are integers, y values are their cubes
x = [1, 2, 3, 4, 5]
y = [number**3 for number in x]

# Styling the plot with a green dotted line and adding a grid
# Change the color to 'magenta', linestyle to 'dashdot', and marker to 'D'
plt.plot(x, y, color='magenta', linestyle='dashdot', marker='D') # altered code
plt.title('Cubic Numbers')
plt.xlabel('Integers')
plt.ylabel('Cubes')
plt.grid(True)
plt.show()

# Time to jazz up our Fibonacci plot! 🚀 Please change the line style to 'solid' ('-') and the line color to orange. Remember, small touches can make a significant difference in how we read and interpret data visually. Are you ready to apply some style?

# Fibonacci sequence values
fib_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
plt.plot(range(len(fib_numbers)), fib_numbers, color='orange', linestyle='solid', marker='_') # altered code
plt.title('Fibonacci Sequence')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)
plt.show()

# Well done, Space Voyager! Now, let's make our plot pop with a bit of beauty. Can you fill in the blanks to style our plot with any style you like?

# Fibonacci sequence values
x = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
y = [0, 1, 1, 2, 4, 8, 16, 32, 64, 128]

# TODO: Call the plot command with any styling you like
plt.plot(x, y, color='darkblue', linestyle='dashdot', marker='*', label='Fibonacci')
# TODO: Add a grid to help estimate the values better and set titles and labels to make the plot informative
plt.title('Fibonacci Etimate Values')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)

plt.show()