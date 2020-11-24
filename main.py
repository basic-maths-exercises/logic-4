import numpy as np

def numberBetween( data, a, b ) : 
  # You need to write code here



# This code allows you to see if your functions are working correctly
data = np.loadtxt("mydata.dat")
print( numberBetween(data,2,5), "of the integers in mydata.dat are between 2 and 5" )
print( numberBetween(data,5,9), "of the integers in mydata.dat are between 5 and 9" )
