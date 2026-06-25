import pandas as pd

students = {
    "Name": ["Senses", "ACE", "Believe", "HawletPackard"],
    "RollNo": [101, 102, 103, 104],
    "Branch": ["CSE", "ECE", "MECH", "CSE"],
    "City": ["C_ABC", "C_DEF", "C_GHI", "C_JKL"],
}

print("Original Student Dictionary:")
print(students)

dframe = pd.DataFrame(students)

print("\nStudent DataFrame:")
print(dframe)

print("\nShape:", dframe.shape)
print("Columns:", list(dframe.columns))
print("\nBranch column:")
print(dframe["Branch"])

print("\nName and City columns:")
print(dframe[["Name", "City"]])

print("\nRow at index 1 using loc:")
print(dframe.loc[1])

print("\nRow at index 1 using iloc:")
print(dframe.iloc[1])

print("\nRows 1 to 3 using loc:")
print(dframe.loc[1:3])

print("\nRows 1 to 3 using iloc:")
print(dframe.iloc[1:3])

print("\nStudents from CSE:")
print(dframe.loc[dframe["Branch"] == "CSE"])

print("\nName and City for CSE students:")
print(dframe.loc[dframe["Branch"] == "CSE", ["Name", "City"]])
