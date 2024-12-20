# Визначаємо виняток користувача
class GroupLimitExceededError(Exception):
    def __init__(self, message="Неможливо додати більше 10 студентів до групи"):
        self.message = message
        super().__init__(self.message)

# Клас для групи
class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student_name):
        if len(self.students) >= 10:
            raise GroupLimitExceededError()
        self.students.append(student_name)

# Створення об'єкта групи
group = Group()

# Додавання студентів, з обробкою винятку
try:
    for i in range(11):  # Спробуємо додати 11 студентів
        group.add_student(f"Студент {i + 1}")
except GroupLimitExceededError as e:
    print(f"Помилка: {e}")
