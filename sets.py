thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
# 
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
# 
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
# 
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
# 
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
# 
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
# 
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
# 
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
# 
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
# tra ve muc giao nhau
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
# 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)