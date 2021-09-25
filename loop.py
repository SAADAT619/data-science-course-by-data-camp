"""
#while_loop
# Initialize offset
offset=8

# Code the while loop
while offset != 0:
    print("correcting...")
    offset = offset - 1
    print(offset)
-----------------------------------------

#while loop with if else statemnet
# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset>0:
      offset = offset - 1
    else : 
      offset = offset + 1    
    print(offset)
------------------------------------------
#for loop
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for element in areas:
    print(element)
------------------------------------------
#another example of for loop
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index,area in enumerate(areas) :
    print("room "+str(index)+": "+str(area))
-------------------------------------------
#update index in the for loop
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index+1) + ": " + str(area))
------------------------------------------
#loop over the list of the list
# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for x in house :
    print("the " + x[0] + " is " + str(x[1]) + " sqm")
-------------------------------------------
# using item() fucntion
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for key,value in europe.items():
    print("the capital of "+key+" is "+str(value))
----------------------------------------
#sue of nditer
# Import numpy as np
import numpy as np

# For loop over np_height
for height in np.nditer(np_height):
    print(str(height)+" inches")

# For loop over np_baseball
for baseball in np.nditer(np_baseball):
    print(baseball)
------------------------------------------



"""