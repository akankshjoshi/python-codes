import matplotlib.pyplot as plt
data_x = ["Nepal","Delhi","Bihar","USA"]
data_y = [20,40,50,60]

plt.xlabel("CITY")
plt .ylabel("POPULATION")
plt .title("BAR PLOT")

plt.bar(data_x, data_y, color='red')
plt.show()