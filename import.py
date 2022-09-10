import numpy
import numpy as ns
# from numpy import array
# fam=["ba", 1.65, "me", 1.5]
# a_fam=array(fam)
# print(a_fam)
height=[1.70, 1.6]
weight=[65.0, 55.0]
# 
ns_height=ns.array(height)
ns_weight=ns.array(weight)
bmi=ns_weight/ns_height**2
bmi
print(bmi)
# 
numpy_he=ns.array(height)
x=numpy_he+numpy_he
print(x)
# 
z=bmi>22
y=bmi[bmi>22]
print(z)
print(y)