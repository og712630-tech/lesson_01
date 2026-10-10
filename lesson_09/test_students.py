from models import Student


def test_create_student(session):
    """Позитивный тест: добавление студента."""
    student = Student(
        first_name="Иван",
        last_name="Петров",
        email="test.student@example.com",
    )
    session.add(student)
    session.commit()

    # Проверяем, что запись создана и получила id
    assert student.id is not None

    # Удаляем за собой
    session.delete(student)
    session.commit()


def test_update_student(session):
    """Позитивный тест: изменение студента."""
    student = Student(
        first_name="Пётр",
        last_name="Сидоров",
        email="test.update@example.com",
    )
    session.add(student)
    session.commit()

    student.last_name = "Смирнов"
    session.commit()
    session.refresh(student)

    assert student.last_name == "Смирнов"

    session.delete(student)
    session.commit()


def test_delete_student(session):
    """Позитивный тест: удаление студента."""
    student = Student(
        first_name="Удаляемый",
        last_name="Студент",
        email="test.delete@example.com",
    )
    session.add(student)
    session.commit()

    student_id = student.id
    session.delete(student)
    session.commit()

    assert session.get(Student, student_id) is None
