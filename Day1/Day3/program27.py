import sys
l = [10, 20, 30]
print("List:", l)
print("\nUsing __sizeof__():", l.__sizeof__())
print("Using sys.getsizeof():", sys.getsizeof(l))
print("\nMemory after adding elements:")
for i in range(2):
    l.append(i)
    print("List:", l)
    print("__sizeof__:", l.__sizeof__())
    print("getsizeof:", sys.getsizeof(l))