class Student:
    def __init__(self, name, branch, rollno):
        self.name = name
        self.branch = branch
        self.rollno = rollno
    # Getter method
    def get_branch(self):
        return self.branch
    # Setter method
    def set_branch(self, branch):
        self.branch = branch
    # Deleter method
    def del_branch(self):
        self.branch = None
S1 = Student("my", "friend", 111)
S1.set_branch("csm")
print(S1.get_branch())
S1.del_branch()
print(S1.get_branch())