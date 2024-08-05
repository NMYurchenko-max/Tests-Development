from tasks.palindrome import solve
import pytest


@pytest.mark.parametrize("input_phrase, expected_result", [
    ("нажал кабан на баклажан", True),
    ("мама мыла раму", False),
    ("дом как комод", False),
    ("рвал дед лавр", True),
    ("азот калий и лактоза", True),
    ("а собака боса", True),
    ("тонет енот", True),
    ("карман мрак", False),
    ("пуст суп", True)
])
def test_solve(input_phrase, expected_result):
    """
    Тест для проверки функции solve
    """
    result = solve([input_phrase])
    assert (len(result) > 0) == expected_result, f"Неверный результат для фразы '{
        input_phrase}': {result}"
