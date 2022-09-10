import matplotlib.pyplot as plt
help(plt.hist)
values = [0,0.6,1.2,1.8,2.4]
plt.hist(values, bins=10)
plt.show()
plt.clf()