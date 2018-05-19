from collections import OrderedDict
from typing import Tuple


class SentimentAnalyzer:
    """ Анализатор тональности текстового контента.

    """
    def analyze(self, web_content: OrderedDict) -> Tuple[int, int, int]:
        """ Проанализировать тональность абзацев заданного веб-контента. Сам веб-контент представляет собой словарь,
        ключами которого являются строковые описания ранее пропарсенных URL-ов, а значениями - списки строк, т.е.
        текстовый контент каждого URL-а, разбитый на последовательность абзацев. Пример:

        {
            "www.abc.com": [
                "мама мыла раму",
                "корова молоко даёт"
            ],
            "https://hello.org": [
                "Здравствуй, мир!",
                "И тебе исполать, добрый молодец!",
                "Доброго здоровьица, девица краса.",
                "Здесь что, все здороваются?"
            ]
        }

        Данный метод анализирует тональность каждого абзаца в каждом URL-е и возвращает три числа: число позитивных
        высказываний (т.е. число абзацев с положительной тональностью), число негативных высказываний (т.е. число
        абзцацев с негативной тональность) и, наконец, общее число всех абзацев.

        :param web_content: словарь текстового контента, разбитого на абзацы, для всех обойдённых URL-ов

        :return Число позитивных высказываний, число негативных высказываний и общее число высказываний.

        """
        pass