d = {}
for i in range(3):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value
print("Dictionary:", d)
k = input("Enter new key: ")
v = input("Enter new value: ")
d[k] = v
print("After Add:", d)
d.update({"City": "Hyderabad"})
print("After Update:", d)
k = input("Enter key to remove: ")
d.pop(k)
print("After Remove:", d)
print("Length:", len(d))
print("Keys:", d.keys())
print("Values:", d.values())
print("Items:", d.items())
d1 = d.copy()
print("Copy:", d1)
d.clear()
print("After Clear:", d)
