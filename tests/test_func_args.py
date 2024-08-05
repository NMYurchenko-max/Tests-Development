from datetime import datetime


def test_function(func, *args, **kwargs):
    """
    Параметры:
    func - функция
    args - позиционные аргументы функции
    kwargs - ключевые аргументы, через него передается ожидание
    """
    result = func(*args, **kwargs)
    try:
        assert result == kwargs.get('expected')
        print("Тест пройден", func.__name__)
    except AssertionError:
        print("Тест не пройден")
    return result


def wrapper(func):
    """
    Проверяет, соответствует ли результат
    выполнения функции ожидаемому значению, переданному
    в виде ключевого аргумента expected.
    Полезна для быстрого тестирования функций с несколькими аргументами
    с предсказуемыми и проверяемыми результатами.
    Однако, обертка не подходит для функций,
    результат которых сложно предсказать/проверить (сравнить)
    (например:работающие с внешними ресурсами или имеющие побочные эффекты),
    или которые не возвращают значения (возвращают None).

    Параметры:
    func - функция на входе
    Возвращает:
    функцию inner - функция с добавленным аргументом expected,
    которая оборачивает логический код приемной функции и проверяет ее работу.
    Не решает исходной ошибки, предоставляет структуру исходной функции
    для обработки вызовов в рамках тестового фреймворка.
    """
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        try:
            assert result == kwargs.get('expected')
            print("Тест пройден", func.__name__)
        except AssertionError:
            print("Тест не пройден")
        return result
    return inner

# Пример использования
# Для функций выполняющих математические операции
# test_function(add, 2, 3, expected=5)


@wrapper
def add(a, b):
    return a + b


add(2, 3, expected=5)  # Тест пройден add
add(2, 3, expected=6)  # Тест не пройден


# Обертка также может быть полезна для функций,
# которые возвращают списки, словари или другие коллекции,
# если ожидаемое значение можно точно определить.
@wrapper
def get_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]


get_even_numbers([1, 2, 3, 4], expected=[2, 4])
# Тест пройден get_even_numbers
get_even_numbers([1, 2, 3, 4], expected=[2, 3])
# Тест не пройден


# Для функций выполняющих преобразования строк
# test_function(convert_to_uppercase, "hello", expected="HELLO")
@wrapper
def convert_to_uppercase(text): return text.upper()


convert_to_uppercase("hello", expected="HELLO")
# Тест пройден convert_to_uppercase
convert_to_uppercase("hello", expected="HELLOO")  # Тест не пройден

# Для функций выполняющих поиск в тексте


@wrapper
def search(text, pattern): return text.find(pattern)


search("hello world", "world", expected=6)  # Тест пройден search
search("hello world", "world", expected=5)  # Тест не пройден

# Для функций выполняющих преобразования дат


@wrapper
def convert_to_date(
    date_string, format): return datetime.strptime(date_string, format)


convert_to_date("2022-01-01", "%Y-%m-%d", expected=datetime(2022, 1, 1))
# Тест пройден convert_to_date
convert_to_date("2022-01-01", "%Y-%m-%d", expected=datetime(2022, 1, 2))
# Тест не пройден

# Обертка подходит для функций,
# которые возвращают True или False,
# если ожидаемое значение также булево.


@wrapper
def is_even(n):
    return n % 2 == 0


is_even(4, expected=True)  # Тест пройден is_even
is_even(5, expected=True)  # Тест не пройден
