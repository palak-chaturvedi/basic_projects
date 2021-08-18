from sympy import *
import numpy as np
  
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
  
  
print("Enter the entries in a single line (separated by space): ")
  
# User input of entries in a 
# single line separated by space
entries = list(map(int, input().split()))
  
# For printing the matrix
a = np.array(entries).reshape(R, C)
print(a)
print("Matrix : {} ".format(M))
   
# Use sympy.rref() method 
M_rref = M.rref()  
      
print("The Row echelon form of matrix M and the pivot columns : {}".format(M_rref))
