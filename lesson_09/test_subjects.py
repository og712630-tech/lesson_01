from models import Subject


def test_create_subject(session):
    """Позитивный тест: добавление предмета."""
    subject = Subject(name="Test Subject", description="Создан для теста")
    session.add(subject)
    session.commit()

    assert subject.id is not None

    session.delete(subject)
    session.commit()


def test_update_subject(session):
    """Позитивный тест: изменение предмета."""
    subject = Subject(name="Old Subject Name")
    session.add(subject)
    session.commit()

    subject.name = "New Subject Name"
    session.commit()
    session.refresh(subject)

    assert subject.name == "New Subject Name"

    session.delete(subject)
    session.commit()


def test_delete_subject(session):
    """Позитивный тест: удаление предмета."""
    subject = Subject(name="Subject to Delete")
    session.add(subject)
    session.commit()

    subject_id = subject.id
    session.delete(subject)
    session.commit()

    assert session.get(Subject, subject_id) is None
