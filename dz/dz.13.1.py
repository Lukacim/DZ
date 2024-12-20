class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Gender: {self.gender}, Age: {self.age}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return (f"{self.first_name} {self.last_name}, Gender: {self.gender}, "
                f"Age: {self.age}, Record Book: {self.record_book}")

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.record_book == other.record_book
        return False

    def __hash__(self):
        return hash(self.record_book)


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student_to_delete = self.find_student(last_name)
        if student_to_delete:
            self.group.remove(student_to_delete)

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f"Group Number: {self.number}\n{all_students}"

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

print(gr)

# Тест пошуку студента
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student), 'Метод поиска должен возвращать экземпляр'

# Тест видалення студента
gr.delete_student('Taylor')
print(gr)  # Only one student


gr.delete_student('Taylor')  # No error!