from typing import Any


def caching_fibonacci():
    # Створюємо порожній словник- кеш
    # Closure
    cache = {}

    def fibonacci(n: int) -> int | Any:
        # За визначенням
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # Перевіряємо, чи є результат уже в кеші
        if n in cache:
            return cache[n]

        # Якщо немає, обчислюємо рекурсивно та записуємо в кеш

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]

    # Повертаємо внутрішню функцію як об'єкт
    return fibonacci


'''
# --- Приклад використання ---

# Створюємо екземпляр функції з  кешем
fib = caching_fibonacci()

# Обчислюємо  число Фібоначчі (вперше)
print(f"Fibonacci(10): {fib(10)}")  

# Обчислюємо 15-те число Фібоначчі
# cache
print(f"Fibonacci(15): {fib(15)}")  
'''
