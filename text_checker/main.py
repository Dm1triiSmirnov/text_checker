import re

import emoji
import pymorphy3


def check_text(text: str) -> bool:
    # Проверка на то что текст состоит из эмодзи
    if emoji.is_emoji(text):
        return True

    # Удаление специальных символов и цифр
    text = re.sub(r"[^a-zA-Zа-яА-ЯёЁ\s]", "", text)

    words: list = text.split()

    # Создание экземпляра для морфологического анализа слов
    morph = pymorphy3.MorphAnalyzer()
    threshold = 0.55

    # Оценка осмысленности слов
    for word in words:
        analized_word = morph.parse(word)
        score = analized_word[0].score
        if score < threshold:
            return False

    # Проверка на количество уникальных слов
    unique_words = set(words)
    if len(unique_words) < 2:
        return False

    return True
