# List of student names
list1 = ["Amit", "Riya", "Jay", "Neha", "Raj"]

# Nested list of names and marks
list2 = [["Amit", 80], ["Riya", 90], ["Jay", 75],
         ["Neha", 85], ["Raj", 95]]

# a) Search student
name = input("Enter student name: ")
if name in list1:
    print("Index:", list1.index(name))
else:
    print("Student not found")

# b) Sort names
list1.sort()
print("Ascending:", list1)
print("Descending:", sorted(list1, reverse=True))

# c) Add, insert and remove
list1.append("Kiran")
list1.insert(1, "Mira")
list1.remove("Jay")
print("Updated list:", list1)

# d) Display student records
for student in list2:
    print(student)

# e) Highest marks and average
highest = max(list2, key=lambda x: x[1])
average = sum(s[1] for s in list2)/len(list2)
print("Highest marks:", highest)
print("Average marks:", average)

# f) Number of records
print("Total records:", len(list2))