f=open("/workspaces/ACE-BOOTCAMP-2026-06/Day5/program52.py","w")
f.write("a=123\nprint(a)")
print("File name:",f.name)
print(f.tell())
f.close()
print(f.closed)
with open("/workspaces/ACE-BOOTCAMP-2026-06/Day5/program52.py","r") as f:
    print(f.read())
print(f.closed)