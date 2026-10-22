# Create a tuple
t = (10, 20, 30, 20, 40, 50, 20, 60, 70, 80)

# a) Display and access elements
print("Tuple:", t)
print("Positive indexing:", t[2])
print("Negative indexing:", t[-1])
print("Slicing:", t[2:6])

# b) Concatenation and repetition
print("Concatenation:", t + (90, 100))
print("Repetition:", t * 2)

# c) Check element
print("20 in tuple:", 20 in t)
print("25 not in tuple:", 25 not in t)

# d) Maximum, minimum and length
print("Maximum:", max(t))
print("Minimum:", min(t))
print("Length:", len(t))

# e) Count occurrences
n = int(input("Enter value to count: "))
print("Occurrences:", t.count(n))

# f) Search element
x = int(input("Enter value to search: "))
if x in t:
    print("Index:", t.index(x))
else:
    print("Element not found")