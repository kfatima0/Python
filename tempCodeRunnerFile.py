print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

#because of this colon 120: the next line is indented. In python spacing and inentation is is really important
#Its tells computer that the code about to write is what should be executed when this condition is met
#if indention is not given indentation error will be shown
if height > 120: 
    print("You can ride the rollercoaster!")
else:
    print("Sorry you have to grow taller before you can ride.")