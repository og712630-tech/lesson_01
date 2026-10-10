def test_get_project_positive(api, created_project):
    """Позитивный тест: получение существующего проекта по ID."""
    response = api.get_project(created_project)

    assert response.status_code == 200, (
        f"Ожидался статус 200, получен {response.status_code}: {response.text}"
    )

    data = response.json()
    assert data["id"] == created_project, "ID проекта не совпадает"
    assert "title" in data, "В ответе отсутствует поле 'title'"


def test_get_project_negative(api):
    """Негативный тест: получение несуществующего проекта."""
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = api.get_project(fake_id)

    # Ожидаем 404 (Not Found) или 400 (Bad Request)
    assert response.status_code in (400, 404), (
        f"Ожидалась ошибка 400/404, получен {response.status_code}: {response.text}"
    )
