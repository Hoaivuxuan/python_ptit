thistuple=("apple","banana","cherry")
print(thistuple)
# 
thistuple1 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple1)
# 
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
# 
thistuple2 = ("apple", "banana", "cherry")
y = ("orange",)
thistuple2 += y
print(thistuple2)
# 
thistuple3 = ("apple", "banana", "cherry")
del thistuple3
print(thistuple3)
# 
fruits = ("apple", "banana", "cherry")
(a, b, c) = fruits
print(a)
print(b)
print(c)
# 
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)