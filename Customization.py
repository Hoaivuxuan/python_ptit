import imp
from pickle import POP
import matplotlib.pyplot as plt
import numpy as np
year = [1950,1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
plt.plot(year, pop)
np_year=np.array(year)
np_year=np_year/8
# 
plt.scatter(year, pop, s=np_year, c = pop)      
# c=color, s=size
plt.xlabel(' Year ')
plt.ylabel(' Population ')
plt.title('World Population Projections')
plt.yticks([0,2,4,6,8,10],
           ['0', '2B', '4B', '6B', '8B', '10B'])
# plt.text(1550, 71, 'India')
# plt.text(5700, 80, 'China')
plt.grid(True)
plt.show()