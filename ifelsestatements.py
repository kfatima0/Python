print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

#because of this colon 120: the next line is indented. In python SPACING and INDENTATION is really important
#Its tells computer that the code about to write is what should be executed when this condition is met
#if indention is not given indentation error will be shown
#elif condition can be included as many as possible

if height >= 120:
       print("You can ride the rollercoster")
       age = int(input("What is your age?"))
       if age <= 12:
              print("Please pay $5.")
       elif age <= 18:
              print("Please pay $7.")
       else:
              print("Please pay $12.")
else:
       print("Sorry you have to grow taller before you can ride.")


#operators
# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

