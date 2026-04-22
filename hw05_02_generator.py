import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генератор, що знаходить усі числа (цілі та дійсні) у тексті.
    """
    # Паттерн  цифри,  може йти крапка і ще цифри
    pattern = r"(?<=\s)\d+(?:\.\d+)?(?=\s)"

    # Для lookaround на межах рядка
    prepared_text = f" {text} "

    # finditer ітерує по збігах, не завантажуючи всі в пам'ять
    for match in re.finditer(pattern, prepared_text):
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Підсумовує числа, отримані від генератора.
    """
    return sum(func(text))

'''
# Тест з цілими та дробовими числами
text = "Дохід 100 за вчора та 25.50 за сьогодні."
print(f"Результат: {sum_profit(text, generator_numbers)}")  # 125.5?

'''