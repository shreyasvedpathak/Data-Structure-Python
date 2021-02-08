class Student:
    '''This is version 1'''

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    
    def __str__(self):
        return 'This is student class'

    def display(self):
        print("Student Name:", self.name)
        print("Student Roll:", self.roll)

s = Student('Shreyas', 12, 87)

s.display()