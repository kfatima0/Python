import numpy as np
mylist =[1,2,3]
type(mylist)
np.array(mylist)
mylist
myarr = np.array(mylist)
type(myarr)
my_matrix = [[1,2,3],[4,5,6],[7,8,9]] ## nested listed
np.array(my_matrix)
np.arange(0,10) #builtin range function
np.arange(0,10,3)
np.zeros(5)
#(shape,dtype=float,order='C') 
#output above array([0., 0., 0., 0., 0.])
np.zeros((5,5))
np.linspace(0,10,11)
#(start,stop,num means how many numebers to declare between start and stop)
np.linspace(0,5,21)
np.eye(5)#identity matrix
np.random.rand(5,2) 
##dot rand it gives  a shape and it will populate it with random samples from a uniform
#distribution over the points 0 to 1 where zero is inclusive and one is exclusive, meaning it can actually
#return back zero, but it can't return back one.
np.random.randn(10)
np.random.randn(6,7)
np.random.randint(0,90,5) #This returns back 5 random integers in between 0,90 
np.random.randint(0,90,(4,5))# This returns 4/5 array 

np.random.seed(101)
np.random.rand(4)

arr = np.arange(0,25)
arr
arr.reshape(5,5) #reshaped above array in 5/5 ,if here its given (5,3) there will be error as we cannot squeeze 25 in 15.So when we multiply these dimensions together, they should equal the same number of elements i had orginally

rarr = np.random.randint(0,101,10)
rarr
rarr.max()
rarr.min()
rarr.argmax()#to know the index location of arry ,93 is in location 1
rarr.argmin()

rarr.dtype
arr
arr.shape # (25,) means to distinguish between having an array kind of as one long row versus one tall column.
arr = arr.reshape(5,5) #here i have reshape by 5/5
arr.shape

##TASK: Create a numpy array of 101 evenly linearly spaced points between 0 and 10. Assign this array to a variable called myarray. Please note, in order for the exercise to evaluate correctly, you must use the variable name myarray.
myarray = np.linspace(0,10,101)
myarray
