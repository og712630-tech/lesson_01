# Lesson 10 — PageObject + Allure

## Установка
pip install -r requirements.txt

Зависимости: selenium, pytest, allure-pytest.

## Запуск тестов с генерацией отчёта
pytest lesson_10/tests --alluredir=./allure-results

## Просмотр отчёта
allure serve ./allure-results