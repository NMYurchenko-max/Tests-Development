import pytest
from tasks.kulinar_book import solve


@pytest.mark.parametrize("cook_book, person, expected_result", [
    (
        [
            ['Салат',
                [
                    ['картофель', 100, 'гр.'],
                    ['морковь', 50, 'гр.'],
                    ['огурцы', 50, 'гр.'],
                    ['горошек', 30, 'гр.'],
                    ['майонез', 70, 'мл.'],
                ]
            ],
            ['Пицца',
                [
                    ['сыр', 50, 'гр.'],
                    ['томаты', 50, 'гр.'],
                    ['тесто', 100, 'гр.'],
                    ['бекон', 30, 'гр.'],
                    ['колбаса', 30, 'гр.'],
                    ['грибы', 20, 'гр.'],
                ],
            ],
            ['Фруктовый десерт',
                [
                    ['хурма', 60, 'гр.'],
                    ['киви', 60, 'гр.'],
                    ['творог', 60, 'гр.'],
                    ['сахар', 10, 'гр.'],
                    ['мед', 50, 'мл.'],
                ]
            ]
        ],
        2,
        ['Салат: картофель 200 гр., морковь 100 гр., огурцы 100 гр., горошек 60 гр., майонез 140 мл.',
        'Пицца: сыр 100 гр., томаты 100 гр., тесто 200 гр., бекон 60 гр., колбаса 60 гр., грибы 40 гр.',
        'Фруктовый десерт: хурма 120 гр., киви 120 гр., творог 120 гр., сахар 20 гр., мед 100 мл.']
    ),
    (
        [
            ['Суп',
                [
                    ['картофель', 200, 'гр.'],
                    ['морковь', 100, 'гр.'],
                    ['лук', 50, 'гр.'],
                    ['мясо', 300, 'гр.'],
                    ['вода', 500, 'мл.'],
                ]
            ],
            ['Омлет',
                [
                    ['яйца', 3, 'шт.'],
                    ['молоко', 50, 'мл.'],
                    ['сыр', 30, 'гр.'],
                    ['помидор', 1, 'шт.'],
                ],
            ]
        ],
        4,
        ['Суп: картофель 800 гр., морковь 400 гр., лук 200 гр., мясо 1200 гр., вода 2000 мл.',
        'Омлет: яйца 12 шт., молоко 200 мл., сыр 120 гр., помидор 4 шт.']
    )
])


def test_solve(cook_book, person, expected_result):
    result = solve(cook_book, person)
    assert result == expected_result, f"Неверный результат: {result}"