# Name (ID): Cooper Chung (Redacted Student ID)
# Lab: B03

from SimpleGraphics import *

# Line 8 - 10 establishes useful constants to ensure the graph is properly drawn

BAR_WIDTH = 100
X_AXIS_LENGTH = 400
Y_AXIS_HEIGHT = 300

# Line 14 - 26 gathers user input for the required parameters stated in the assignment. Integers for bar heights and origin coordinates. Text for title and colours

titleName = input("Enter a title for the graph: ")

barOneHeight = int(input("Enter a height for the first bar: "))
barOneColour = input("Pick a colour for the first bar: ")

barTwoHeight = int(input("Enter a height for the second bar: "))
barTwoColour = input("Pick a colour for the second bar: ")

barThreeHeight = int(input("Enter a height for the third bar: "))
barThreeColour = input("Pick a colour for the third bar: ")

originx = int(input("Enter the x coordinate for the origin: "))
originy = int(input("Enter the y coordinate for the origin: "))

# The height of the title text was arbitrary, but the assignment says it is not included in the height of the chart so I placed the title above the chart so it looks clean

setFont("Arial", "24", "bold")
text(originx + 200, originy - 350, titleName)

# Draws the bars, and sets the colour to the user specified colour
# "originy - bar_____Height" to align all the bars on the x axis and display the correct height from the user input (make the bar draws upwards since the y axis is flipped)
# "originx + 50" is to space the leftmost bar to the right of the y axis by 50 pixels so it looks clean

setColor(barOneColour)
rect(originx + 50, originy - barOneHeight, BAR_WIDTH, barOneHeight)

# "originx + BAR_WIDTH + 50" to correctly place the second bar next to the first, and account for the 50 pixel spacing

setColor(barTwoColour)
rect(originx + BAR_WIDTH + 50, originy - barTwoHeight, BAR_WIDTH, barTwoHeight)

setColor(barThreeColour)
rect(originx + 2 * BAR_WIDTH + 50, originy - barThreeHeight, BAR_WIDTH, barThreeHeight)

# Draws the x axis

setColor("black") # This line is necessary or else the x axis will be the same colour as the third bar
line(originx, originy, originx + X_AXIS_LENGTH, originy) 

# To draw the y axis upward from the user set origin we subtract the height instead of adding, also to make sure the height of the chart is 300 pixels

setColor("black")
line(originx, originy, originx, originy - Y_AXIS_HEIGHT)