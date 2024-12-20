
class Student:
    def __init__(self, gender, age, first_name, last_name, student_id):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return str(self) == str(other)
        return False

    def __hash__(self):
    
        return hash(str(self))


class Group:
    def __init__(self, name):
        self.name = name
        self.students = set()  

    def add_student(self, student):
        self.students.add(student)

    def delete_student(self, last_name):
        self.students = {student for student in self.students if student.last_name != last_name}

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        return f"Group {self.name} with students: {', '.join(str(student) for student in self.students)}"

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)


print(gr)

assert gr.find_student('Jobs') == st1  #
assert gr.find_student('Jobs2') is None  

gr.delete_student('Taylor')
print(gr)  
