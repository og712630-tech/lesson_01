import requests
from config import BASE_URL, HEADERS


class YougileProjectsAPI:
    """Обёртка над методами работы с проектами YouGile."""

    def __init__(self):
        self.base_url = BASE_URL
        self.headers = HEADERS
        self.project_id = None

    def create_project(self, title: str, users: dict = None):
        """[POST] /api-v2/projects — создание проекта."""
        payload = {"title": title}
        if users:
            payload["users"] = users
        return requests.post(
            f"{self.base_url}/projects",
            json=payload,
            headers=self.headers
        )

    def get_project(self, project_id: str):
        """[GET] /api-v2/projects/{id} — получение проекта по ID."""
        return requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers
        )

    def update_project(self, project_id: str, payload: dict):
        """[PUT] /api-v2/projects/{id} — обновление проекта."""
        return requests.put(
            f"{self.base_url}/projects/{project_id}",
            json=payload,
            headers=self.headers
        )

    def create_and_return_id(self, title: str) -> str:
        """Создаёт проект и возвращает его ID."""
        response = self.create_project(title)
        assert response.status_code == 201, (
            f"Не удалось создать проект: {response.status_code} {response.text}"
        )
        self.project_id = response.json()["id"]
        return self.project_id
