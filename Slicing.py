"""
Slicing in Python
slicing is a technique used to extract a portion of a sequence (like a list, tuple, or string)
by specifying a start index, an end index, and an optional step value. 
The syntax for slicing is as follows:
sequence[start:end:step]
PYTHON
"""""""""""

#Postive Slicing
name = "Python"
print(name[0:3]) # Output: Pyt
print(name[2:5]) # Output: tho
print(name[1:]) # Output: ython

#Negative Slicing
name = "Python"
print(name[-6:-3]) # Output: Pyt
print(name[-4:-1]) # Output: tho
print(name[-5:]) # Output: ython

#Slicing with Step
name = "Python" 
print(name[0:6:2]) # Output: Pto
print(name[1:6:2]) # Output: yhn

#Reversing a String using Slicing
name = "Python"
print(name[::-1]) # Output: nohtyP
print(name[5:0:-1]) # Output: nohty