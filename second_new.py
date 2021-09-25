"""
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr=cars['drives_right']

# Use dr to subset cars: sel
sel= cars[dr]

# Print sel
print(sel)
--------------------------------------
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
dr = cars['drives_right']
sel = cars[dr]

# Print sel
print(sel)
print(sel)
------------------------------------------

#how to write the previous code in one line
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
sel = cars[cars['drives_right']]

# Print sel
print(sel)
"""