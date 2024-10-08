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