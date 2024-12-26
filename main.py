def count_vowels(some_text: str) -> int:

    if some_text == '':
        return 0

    vowels: str = 'аеёиоуыэюяaeiouy'
    vowel_count: int = 0

    for char in some_text.lower():
        if char in vowels:
            vowel_count += 1

    return vowel_count


# Пример использования
# user_text: str = input('Введите слово, словосочетание или предложение: ')
# vowels_amount: int = count_vowels(user_text)
# print(f'Количество гласных букв в тексте: {vowels_amount}')