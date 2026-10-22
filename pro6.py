from array import *

a = array('i', [10, 20, 30, 40, 50, 60, 70, 80])

# a) Display, indexing and slicing
print("Array:", a)
print("Element at index 2:", a[2])
print("Slicing:", a[1:4])

# b) Insert an element
a.insert(2, 25)
print("After insert:", a)

# c) Remove and pop
a.remove(40)
a.pop()
print("After remove and pop:", a)

# d) Search an element
x = int(input("Enter element to search: "))
if x in a:
    print("Index:", a.index(x))
else:
    print("Element not found")

# e) Membership
print(20 in a)
print(100 not in a)

# f) Maximum, minimum and length
print("Maximum:", max(a))
print("Minimum:", min(a))
print("Length:", len(a))

# g) Reverse array
a.reverse()
print("Reversed array:", a)