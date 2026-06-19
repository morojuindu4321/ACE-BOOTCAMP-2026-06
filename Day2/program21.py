# 1. APPEND()
print("APPEND")
list1 = []
for i in range(5):
    list1.append(int(input("Enter element: ")))
num = int(input("Enter number to append: "))
list1.append(num)
print(list1)
# 2. INSERT()
print("\nINSERT")
list1 = []
for i in range(5):
    list1.append(int(input("Enter element: ")))
index = int(input("Enter index: "))
num = int(input("Enter number: "))
list1.insert(index, num)
print(list1)
# 3. EXTEND()
print("\nEXTEND")
list1 = []
list2 = []
for i in range(3):
    list1.append(int(input("Enter List1 element: ")))
for i in range(3):
    list2.append(int(input("Enter List2 element: ")))
list1.extend(list2)
print(list1)
# 4. REMOVE()
print("\nREMOVE")
list1 = []
for i in range(5):
    list1.append(int(input("Enter element: ")))
num = int(input("Enter number to remove: "))
list1.remove(num)
print(list1)
# 5. POP()
print("\nPOP")
list1 = []
for i in range(5):
    list1.append(int(input("Enter element: ")))
index = int(input("Enter index: "))
list1.pop(index)
print(list1)
# 6. CLEAR()
print("\nCLEAR")
list1 = []
for i in range(5):
    list1.append(int(input("Enter element: ")))
list1.clear()
print(list1)
# 7. DEL
print("\nDEL")
list1 = []
for i in range(5):
    list1.append(int(input("Enter element: ")))
index = int(input("Enter index: "))
del list1[index]
print(list1)
# 8. INDEX()
print("\nINDEX")
list1 = []
for i in range(5):
    list1.append(int(input("Enter element: ")))
num = int(input("Enter number: "))
print(list1.index(num))
# 9. COUNT()
print("\nCOUNT")
list1 = []
for i in range(5):
    list1.append(int(input("Enter element: ")))
num = int(input("Enter number: "))
print(list1.count(num))
# 10. SORT()
print("\nSORT")
list1 = []
for i in range(5):
    list1.append(int(input("Enter element: ")))
list1.sort()
print(list1)
# 11. REVERSE()
print("\nREVERSE")
list1 = []
for i in range(5):
    list1.append(int(input("Enter element: ")))
list1.reverse()
print(list1)
# 12. COPY()
print("\nCOPY")
list1 = []
for i in range(5):
    list1.append(int(input("Enter element: ")))
list2 = list1.copy()
print(list2)
# 13. LEN()
print("\nLEN")
list1 = []
for i in range(5):
    list1.append(int(input("Enter element: ")))
print(len(list1))
# 14. MAX()
print("\nMAX")
list1 = []
for i in range(5):
    list1.append(int(input("Enter element: ")))
print(max(list1))
# 15. MIN()
print("\nMIN")
list1 = []
for i in range(5):
    list1.append(int(input("Enter element: ")))
print(min(list1))
# 16. SUM()
print("\nSUM")
list1 = []
for i in range(5):
    list1.append(int(input("Enter element: ")))
print(sum(list1))
