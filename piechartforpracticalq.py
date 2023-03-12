import matplotlib.pyplot as plt
import numpy as np
cars = ["AUDI","BMW","TESLA","JAGUAR","MERCEDES"]
data = [23,54,66,12,55]
fig = plt.figure(figsize=(10,7))
plt.pie(data, labels = cars)
plt.show()