
def solve(phrases: list):
    result = []  # список палиндромов
    for phrase in phrases:
        # пройдите циклом по всем фразам
        clean_phrase = phrase.replace(" ", "").lower()
        # удаляем пробелы и приводим к нижнему регистру
        if clean_phrase == clean_phrase[::-1]:
            result.append(phrase)
    return result
