def test_create_project_positive(api):
    """Позитивный тест: создание проекта с валидным названием."""
    response = api.create_project("My New Project")

    assert response.status_code == 201, (
        f"Ожидался статус 201, получен {response.status_code}: {response.text}"
    )

    data = response.json()
    assert "id" in data, "В ответе отсутствует поле 'id'"
    assert isinstance(data["id"], str), "Поле 'id' должно быть строкой"


def test_create_project_negative(api):
    """Негативный тест: создание проекта без обязательного поля title."""
    response = api.create_project(title="")  # пустое название

    # Ожидаем ошибку 400 (Bad Request) или 422 (Unprocessable Entity)
    assert response.status_code in (400, 422), (
        f"Ожидалась ошибка 400/422, получен {response.status_code}: {response.text}"
    )
