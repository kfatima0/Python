#goal to create python pizza delivery program and the program is going to automatically calculate the bill for the user on a number of options
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
customize_toppings = input("Do you want customizetoppings on our pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

#todo: workout how much they need to pay based on their size choice
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong inputs.")


#todo: workout how much to add to their bill based on their customize toppings choice.
if customize_toppings == "Y":
    if size == "S":
       bill += 2
    else: 
        bill += 3

#todo: work out their final mount based on whether if they want extra cheese.
if extra_cheese == "Y":
    bill += 1

print("Your final bill is: ${bill}.")
