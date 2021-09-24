class college:
    def __init__(self):
        self.name = str
        self.age = int
        self.roll_no = int
        self.branch = str
        self.students = {}
    
    def add_student(self, n, r, a, b):
        self.name = n
        self.age = a
        self.roll_no = r
        self.branch = b
        self.add_to_dictionary()

    def add_to_dictionary(self):
        self.students[self.roll_no] = {
            'name': self.name,
            'roll': self.roll_no,
            'age': self.age,
            'branch': self.branch
        }

    def queries(self,roll1, roll2, detail):
        print(self.students[roll1])
        print(self.students[roll2][detail])

if __name__ == '__main__':

    obj = college()
    obj.add_student('Abhishek', 101, 21, 'CSE')
    obj.add_student('Arun', 109, 22, 'ME')
    obj.add_student('Priyanka', 111, 20, 'Arts')
    obj.add_student('Aarti', 100, 22, 'Literature')

    obj.queries(111, 100, 'branch')