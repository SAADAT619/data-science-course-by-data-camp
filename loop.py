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
"""