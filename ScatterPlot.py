import matplotlib.pyplot as plt
year = [1950,1970, 1990, 2010]
num_pep = [2.519, 3.692, 5.263, 6.972]
plt.plot(year, num_pep)
plt.scatter(year, num_pep)
plt.xscale('log')
plt.show()  