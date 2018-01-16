import math
wallWidth = math.ceil(float(input('please enter the width of the wall in feet: ').strip()))
wallHeight = math.ceil(float(input('please enter the height of the wall in feet: ').strip()))
paintCost = float(input('please enter the price of a gallon of the paint you would like to use: $ ').strip())

projectCost = wallWidth * wallHeight * paintCost

print("your project will cost ${} ".format(projectCost))
