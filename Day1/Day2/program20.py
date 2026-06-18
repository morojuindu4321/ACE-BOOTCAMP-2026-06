# Tuple and Tuple Handling Functions

t = (10, 20, 30, 40, 20)

print("Tuple:", t)

# Built-in Functions
print("Length:", len(t))
print("Maximum:", max(t))
print("Minimum:", min(t))
print("Sum:", sum(t))
print("Sorted Tuple:", sorted(t))

# Tuple Methods
print("Count of 20:", t.count(20))
print("Index of 30:", t.index(30))

# Creating a Tuple using tuple()
lst = [1, 2, 3, 4]
new_tuple = tuple(lst)
print("Tuple from List:", new_tuple)