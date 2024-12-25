import pytest
from main import count_vowels


def test1_count_vowels():
    assert count_vowels('hello') == 2
    assert count_vowels('world') == 2
    assert count_vowels('свобода') == 3


@pytest.mark.parametrize('text, expected', [
    ('Стол', 1),
    ('Book', 2),
    ('Автомобиль', 4),
    ('Tree', 2),
    ('Окно', 2),
    ('Sea', 2),
    ('Город', 2),
    ('Bird', 1),
    ('Река', 2),
    ('Computer', 3),
    ('Шмрц', 0),  # Чешский мотогонщик Якуб Шмрц
    ('Ааа Oоо You', 9)  # Смесь русских и латинских символов
])
def test2_count_vowels(text, expected):
    assert count_vowels(text) == expected