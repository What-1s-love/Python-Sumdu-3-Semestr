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
