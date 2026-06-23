class Student:
    def __init__(self,name,branch,rollno):
        self.name=name
        self.branch=branch
        self.rollno=rollno
    @property
    def from_branch(self):
        return self.branch
    @from_branch.setter   
    def from_branch(self, branch):
        self.branch = branch
    @from_branch.deleter
    def from_branch(self):
        self.branch = None
s1 = Student("My","CSM",111)
print(s1.from_branch)
s1.from_branch = "CSit"
print(s1.from_branch)
del s1.from_branch
print(s1.from_branch)