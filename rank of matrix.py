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



rank = np.linalg.matrix_rank(a)

print('Matrix : ', a)
print('Rank of the given Matrix : ',rank)
