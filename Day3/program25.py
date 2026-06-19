import copy
original = [1, 2, [3, 4]]
shallow = copy.copy(original)
print("Before change:")
print("Original:", original)
print("Shallow :", shallow)
shallow[0] = 100
shallow[2][0] = 999
print("\nAfter change:")
print("Original:", original)
print("Shallow :", shallow)
