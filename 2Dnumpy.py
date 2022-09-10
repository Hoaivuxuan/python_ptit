from numpy import array
np_2d=array([[1.73,1.70], [1.50, 1.55]])
np_2d
print(np_2d)
x=np_2d.shape
print(x)
# 
print(np_2d[0])
print(np_2d[0][1])
print(np_2d[0,1])
print(np_2d[:,1:2])
print(np_2d[1,:])
