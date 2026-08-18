import pytest
from string_utils import StringUtils

# Инициализация объекта для тестов
utils = StringUtils()

# ==================== Тесты для capitalize ====================

@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),          # позитивный: обычное слово
    ("SKYPRO", "Skypro"),          # позитивный: все заглавные
    ("sKyPrO", "Skypro"),          # позитивный: смешанный регистр
    ("123abc", "123abc"),          # негативный: начинается с цифры
    ("", ""),                      # пограничный: пустая строка
    (" ", " "),                    # пограничный: только пробел
])
def test_capitalize(input_str, expected):
    assert utils.capitalize(input_str) == expected

# ==================== Тесты для trim ====================

@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),       # позитивный: пробелы в начале
    ("skypro", "skypro"),          # позитивный: без пробелов
    ("   sky   pro", "sky   pro"), # позитивный: пробелы внутри
    ("", ""),                      # пограничный: пустая строка
    ("   ", ""),                   # пограничный: только пробелы
])
def test_trim(input_str, expected):
    assert utils.trim(input_str) == expected

# ==================== Тесты для contains ====================

@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),         # позитивный: символ в начале
    ("SkyPro", "o", True),         # позитивный: символ в середине
    ("SkyPro", "y", True),         # позитивный: символ есть
    ("SkyPro", "U", False),        # негативный: символа нет
    ("", "a", False),              # негативный: пустая строка
    ("abc", "", False),            # пограничный: пустой символ (ожидаем False)
])
def test_contains(string, symbol, expected):
    assert utils.contains(string, symbol) == expected

# ==================== Тесты для delete_symbol ====================

@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),      # позитивный: удаление буквы
    ("SkyPro", "Pro", "Sky"),      # позитивный: удаление подстроки
    ("SkyPro", "S", "kyPro"),      # позитивный: удаление первой буквы
    ("SkyPro", "z", "SkyPro"),     # негативный: символа нет (строка не меняется)
    ("", "a", ""),                 # пограничный: пустая строка
    ("abc", "", "abc"),            # пограничный: пустой символ (ничего не удаляем)
    ("aaa", "a", ""),              # позитивный: удаление всех вхождений
])
def test_delete_symbol(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected
