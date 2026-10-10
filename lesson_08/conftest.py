import pytest
from yougile_api import YougileProjectsAPI


@pytest.fixture
def api():
    """Фикстура, возвращающая экземпляр API-клиента."""
    return YougileProjectsAPI()


@pytest.fixture
def created_project(api):
    """Фикстура: создаёт проект и возвращает его ID, чтобы не дублировать код."""
    project_id = api.create_and_return_id("Test Project Fixture")
    yield project_id
    # Опционально: удаление проекта после теста
    # api.update_project(project_id, {"deleted": True})
