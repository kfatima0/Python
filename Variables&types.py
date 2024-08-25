### When a program is executing, the program code itself is stored in one part of memory, 
### the data it interacts with is stored in another area of memory, and so on.
###few rules for variable names: 
    #python variable names must begin witha letter (either upper or lower case) or an underscore_character
    #can contain letters , numbers or underscore characters(but cannot begin with a number)
    #python variables are case senestive,so greeting and Greeting refers 2 different variables
    #variables are created when they are first attached to a valu, unsing =

greeting = "Hello"
name =  "Fatima"

print(greeting + name)
print(greeting + ' ' + name)

age = 24## here python stores the value somewhere, type of the value is int, its an integer value
##here bound the name age to it , which makes age have the type int,
##in python we can rebind a name to different value
print(age)

age = "2years" ##here the string value 2years in memory and binds label age to it.
## its not possible in many other languages
## once a variable has a type , you can only assign values of that type to it.
## java and C are examples of languages that behave in this way
##here age is bound to a string value. its no longer an int,its a string
print(age)
## here in line 20 looks like we are assigning the string value two years to a variable called age and
## its true in languages C and java
## in python its more helpful to say we have rebound the label age to string value 2 years
print(name + " is " + age + " years old")

##python built-in data types are -
##numeric iterator, sequence(which are also iterators), mapping file ,class exception
##python 3 has numeric data types - int ,float complex
##python 2 had another type , long because its int type couldnt store 
## in python 3 int type replaces long
## in python 3 int effectively has no maximum size
## python floats have 52 digits of precision


#EXPRESSIONS
a = 12# they are not expressions
b = 3

print (a + b) # Python evaluates a to get the value 12, and b to get the value 3.
#It then adds them, evaluating the expression 12 + 3, and the same thing happens on lines 45 through 49.
#So expressions can themselves, be made up of expressions.
print (a - b)
print (a * b)
print (a / b)
print (a // b)
print (a % b) # integer division, rounded down towards minus infinity
print(a % b)


for i in range(1, 4):
     print(i)

for i in range(1, a / b): #error-float object cannot be interpreted as an integer 
#to perform integer divison using two forward slashed instead of one this error occurs
    print(i)

#Python is strongly typed, we cant use float in places where int must be used    
for i in range(1, a // b): #two expressions
    print(i)
# here in line 57 we've got the literal value 1 inside the parentheses and it evaluates, to the value 1,
# but again, it's still an expression.Now also inside the parentheses,we've got a a integer divide by b, 
#and that's the two slashes.At the moment, that evaluates to 4 because a is currently 12 and b is 3.
# two expressions found till now but there are more
# the two expressions we've identified are part of another expression.so the code range parentheses, 
#and then it's 1, a // by b. That evaluates to a range of numbers from 1 to 3.
# python has to evaluate that, in order to work out what values to use in the loop.
# it evaluates the expression 1 to get the value 1, and then a // b to get the value 4.
#once it's done that, it has to evaluate range(1, 4).So that's another expression.
# another expression on line 59
#The variable i has to be evaluated so that Python knows what to print.
#The first time around the loop, it evaluates to the value 1, next time around it's 2 and the last time
# around it evaluates to 3.
# in line 63 i is not an expression i is being bound to each of the values produced by range in turn
# code of line 63 is written  below long handed instead of using a for loop, 

i = 1
print(i)
i = 2
print(i)
i = 3
print (i)
#here 6 lines of code exactly does the same thing of 63 and 64










