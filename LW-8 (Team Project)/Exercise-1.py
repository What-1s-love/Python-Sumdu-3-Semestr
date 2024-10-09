# Автор: Натан Недайхліб (Студент 1)

# Створення словника для зберігання інформації про успішність студентів групи
students_performance = {
    "group_number": "101",
    "students": [
        {
            "full_name": "Іванов Іван Іванович",
            "course": 2,
            "subjects_grades": {
                "Математика": 85,
                "Фізика": 90,
                "Програмування": 95
            }
        },
        {
            "full_name": "Петров Петро Петрович",
            "course": 2,
            "subjects_grades": {
                "Математика": 78,
                "Фізика": 82,
                "Програмування": 88
            }
        }
        # Можна додавати більше студентів
    ]
}

def add_student(performance_dict, full_name, course, subjects_grades):
    """
    Функція для додавання нового студента до словника успішності.
    
    :param performance_dict: словник з інформацією про групу
    :param full_name: повне ім'я студента
    :param course: курс студента
    :param subjects_grades: словник предметів та оцінок
    """
    new_student = {
        "full_name": full_name,
        "course": course,
        "subjects_grades": subjects_grades
    }
    performance_dict["students"].append(new_student)
    print(f"Студента {full_name} успішно додано.")

# Приклад використання функції
add_student(
    students_performance,
    "Сидоров Сидір Сидорович",
    2,
    {
        "Математика": 80,
        "Фізика": 85,
        "Програмування": 90
    }
)

# Шаповал Анастасія (Студентка 2) додала вивід словника про студентів та функцію сортування даних, 
# а саме сортування студентів за оцінкою з конкретного предмета Математики.

def print_students(students, title="Список студентів", show_grades=True):
    """
    Функція для виведення списку студентів з їхніми оцінками.
    
    :param students: список студентів
    :param title: заголовок для виведення
    :param show_grades: прапорець для виведення оцінок за кожний предмет (True)
    """
    print(f"\n{title}:")
    for student in students:
        if show_grades:
            grades = ", ".join(f"{subject}: {grade}" for subject, grade in student['subjects_grades'].items())
            print(f"{student['full_name']} (Курс {student['course']}): {grades}")

def sort_students_by_subject(students, subject):
    """
    Функція для сортування студентів за оцінкою з конкретного предмета Математики.
    
    :param students: список студентів
    :param subject: предмет, за яким потрібно виконати сортування
    :return: відсортований список студентів
    """
    return sorted(students, key=lambda s: s['subjects_grades'].get(subject, 0), reverse=True)

# Виведення студентів перед сортуванням
print_students(students_performance['students'], "Список студентів перед сортуванням")

# Використання функції для сортування за оцінкою з математики
sorted_by_math = sort_students_by_subject(students_performance['students'], 'Математика')

# Виведення відсортованих студентів з оцінками з математики
print_students(sorted_by_math, "Список студентів після сортування за оцінкою з Математики", show_grades=True)

# Суков Микола (Студент 3) додав оновлення оцінки яка дозволяє змінити оцінку студента з конкретного предмета,
# а також виведення середнього балу кожного студента за всіма предметами.
# Нова функція для оновлення оцінки студента
def update_grade(students, full_name, subject, new_grade):
    """
    Оновлює оцінку студента за конкретним предметом.
    
    :param students: список студентів
    :param full_name: ім'я студента
    :param subject: предмет, який потрібно оновити
    :param new_grade: нова оцінка
    """
    for student in students:
        if student['full_name'] == full_name:
            student['subjects_grades'][subject] = new_grade
            print(f"\nОцінку з предмета {subject} для студента {full_name} успішно оновлено на {new_grade}.")
            return
    print(f"Студента з ім'ям {full_name} не знайдено.")

# Нова функція для виведення середнього балу
def print_average_grades(students):
    """
    Виводить середній бал кожного студента за всіма предметами.
    
    :param students: список студентів
    """
    for student in students:
        grades = student['subjects_grades'].values()
        average_grade = sum(grades) / len(grades)
        print(f"{student['full_name']} має середній бал: {average_grade:.2f}")

# Виведення студентів перед сортуванням
print_students(students_performance['students'], "Список студентів перед сортуванням")

# Сортування за оцінкою з математики
sorted_by_math = sort_students_by_subject(students_performance['students'], 'Математика')

# Виведення відсортованих студентів
print_students(sorted_by_math, "Список студентів після сортування за оцінкою з Математики", show_grades=True)

# Оновлення оцінки з математики для студента Іванов Іван Іванович
update_grade(students_performance['students'], "Іванов Іван Іванович", "Математика", 92)

# Виведення середнього балу кожного студента
print("\nСередні бали студентів:")
print_average_grades(students_performance['students'])
