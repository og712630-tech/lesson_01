from models import Teacher


def test_create_teacher(session):
    """Позитивный тест: добавление преподавателя."""
    teacher = Teacher(
        first_name="Сергей",
        last_name="Иванов",
        email="test.teacher@example.com",
    )
    session.add(teacher)
    session.commit()

    assert teacher.id is not None

    session.delete(teacher)
    session.commit()


def test_update_teacher(session):
    """Позитивный тест: изменение преподавателя."""
    teacher = Teacher(
        first_name="Анна",
        last_name="Козлова",
        email="test.update.teacher@example.com",
    )
    session.add(teacher)
    session.commit()

    teacher.first_name = "Мария"
    session.commit()
    session.refresh(teacher)

    assert teacher.first_name == "Мария"

    session.delete(teacher)
    session.commit()


def test_delete_teacher(session):
    """Позитивный тест: удаление преподавателя."""
    teacher = Teacher(
        first_name="Удаляемый",
        last_name="Преподаватель",
        email="test.delete.teacher@example.com",
    )
    session.add(teacher)
    session.commit()

    teacher_id = teacher.id
    session.delete(teacher)
    session.commit()

    assert session.get(Teacher, teacher_id) is None
