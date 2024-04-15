# Topic Overview and Actualization
# Welcome! Today's lesson is all about styling plots. Styling is essential for making plots visually attractive and informative. We'll walk through various styling plot aspects with Python's Matplotlib, enhancing a simple line plot as we progress. Let's get started!

# Basic Plot
# In Matplotlib, each plot line defaults to a specific color and line type. Here's an example with a basic line plot:

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)
plt.show()

# Adjusting Colors and Line Types
# Ever want to change these defaults? Fortunately, Matplotlib lets you do just that with the color and linestyle parameters:

plt.plot(x, y, color='red', linestyle='dashed')
plt.show()

# Voila! Our line is now red and dashed!

# Here's the fun part: Matplotlib offers many color options (like 'green', 'blue', 'cyan', etc.) and line styles (like 'solid', 'dotted', 'dashdot', etc.). This feature allows for more personalized and differentiated line plots.

# Adding Markers
# Markers can significantly enhance the aesthetics and readability of your plot by highlighting the data points. Matplotlib allows us to add markers using the marker parameter:

plt.plot(x, y, color='black', linestyle='solid', marker='o')
plt.show()

# Some commonly used markers include 'o' (circle), '.' (point), '*' (star), 's' (square), '+' (plus), 'x' (cross), etc.

# Adding Titles, Labels, and Legends
# Good labels make plots easy to understand. So, let's add a title, x-label, y-label, and a legend to make our plot more self-explanatory:

plt.plot(x, y, color='red', linestyle='dashed')
plt.title('Square Numbers') # Title of the plot
plt.xlabel('Numbers') # x-axis label
plt.ylabel('Squares') # y-axis label
plt.legend(['Square Numbers']) # Legend
plt.show()

# Now, our plot carries much more information!

# Setting Axes Limits and Ticks
# You may want to focus on a particular region in your plot. Matplotlib allows us to limit the ranges shown on the x- and y-axes using xlim() and ylim(). Additionally, it allows us to set the tick marks using xticks() and yticks(). Let's try them out:

plt.plot(x, y, color='red', linestyle='dashed')
plt.title('Square Numbers')
plt.xlabel('Numbers')
plt.ylabel('Squares')
plt.legend(['Square Numbers'])
plt.xlim(2, 5) # Limit on x-axis
plt.ylim(4, 25) # Limit on y-axis
plt.xticks(range(2, 6)) # Ticks on x-axis
plt.yticks(range(4, 26, 5)) # Ticks on y-axis
plt.show()

# We pass the lower and upper limits of the x and y axes in the xlim and ylim functions. xticks and yticks functions take exact ticks locations as an argument. Ticks are usually evenly spaced so we can set their locations with range.

# Our plot now displays squares for numbers from 2 to 5.

# Adding Gridlines
# Gridlines provide an easier way to estimate values in plots. To add them, we use grid(True):

plt.plot(x, y, color='red', linestyle='dashed')
plt.title('Square Numbers')
plt.xlabel('Numbers')
plt.ylabel('Squares')
plt.legend(['Square Numbers'])
plt.xlim(1, 6)
plt.ylim(1, 30)
plt.xticks(range(1, 7))
plt.yticks(range(0, 31, 5))
plt.grid(True) # Adding gridlines
plt.show()

# With the gridlines turned on, our plot becomes more precise!