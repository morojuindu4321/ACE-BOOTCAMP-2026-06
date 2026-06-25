import pandas as pd
students={
   "Name": ['Senses', 'ACE', 'Believe', 'HawletPackard'],
    "RollNo": [101, 102, 103, 104],
    "Branch": ['CSE', 'ECE', 'MECH', 'CSE'],
    "City": ['C_ABC', 'C_DEF', 'C_GHI', 'C_JKL']
}
print(students)
dframe=pd.DataFrame(students)
print(dframe)
print(dframe.shape)
print(dframe.columns)
print(dframe['Branch'])
print(dframe[['Name','City']])
print(dframe.loc[1])
print(dframe.iloc[1])
print(dframe.loc[1:3])
print(dframe.iloc[1:3])
print(dframe.loc[dframe['Branch']=='CSE'])
print(dframe.loc[dframe['Branch']=='CSE',['Name','City']])