# main.py

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
        # Порівнюємо студентів за їх іменами та прізвищами
        if isinstance(other, Student):
            return str(self) == str(other)
        return False

    def __hash__(self):
        # Хешування за рядковим представленням студента
        return hash(str(self))


class Group:
    def __init__(self, name):
        self.name = name
        self.students = set()  # використовуємо set, бо студенти тепер можуть бути хешованими

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


# Створення студентів та групи
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')

# Додавання студентів до групи
gr.add_student(st1)
gr.add_student(st2)

# Виведення групи
print(gr)

# Тестування пошуку студента
assert gr.find_student('Jobs') == st1  # Повертає студентів з іменем Jobs
assert gr.find_student('Jobs2') is None  # Не знайдено студента з таким прізвищем

# Видалення студента з групи
gr.delete_student('Taylor')
print(gr)  # Лише один студент залишиться
