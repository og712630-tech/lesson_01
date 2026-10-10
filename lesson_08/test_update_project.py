def test_update_project_positive(api, created_project):
    """Позитивный тест: обновление названия проекта."""
    new_title = "Updated Project Title"
    response = api.update_project(
        created_project,
        {"title": new_title}
    )

    assert response.status_code == 200, (
        f"Ожидался статус 200, получен {response.status_code}: {response.text}"
    )

    # Проверяем, что изменение применилось
    check_response = api.get_project(created_project)
    assert check_response.status_code == 200
    assert check_response.json()["title"] == new_title, (
        "Название проекта не обновилось"
    )


def test_update_project_negative(api):
    """Негативный тест: обновление несуществующего проекта."""
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = api.update_project(
        fake_id,
        {"title": "New Title"}
    )

    assert response.status_code in (400, 404), (
        f"Ожидалась ошибка 400/404, получен {response.status_code}: {response.text}"
    )
