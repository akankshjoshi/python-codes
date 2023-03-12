import numpy as np
the_array = ([[1,2], [3,4]])
colums_to_append = [5,6]
the_array = np.insert(the_array, 2, colums_to_append, axis=1)
print(the_array)