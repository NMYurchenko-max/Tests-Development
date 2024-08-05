import pytest
from tasks.secretary import get_name, get_directory, add


@pytest.fixture(scope="module")
# Фикструра для инициализации начальных данных,
# данный метод будет вызываться каждый раз перед тестами
def init_data():
    # Создается набор документов и директорий
    documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"}
    ]
    directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
    }
    return documents, directories


# Параметрический тест для функции get_name
@pytest.mark.parametrize("doc_number,expected_name", [
    ("2207 876234", "Василий Гупкин"),
    ("11-2", "Геннадий Покемонов"),
    ("10006", "Аристарх Павлов"),
    ("5455 028765", "Василий Иванов"),
    ("99999", "Документ не найден")
    # Тестовый случай отсутствия документа
])
def test_get_name(init_data, doc_number, expected_name):
    documents, _ = init_data
    # Проверка на соответствие ожидаемому значению имени владельца документа,
    # полученному с помощью функции get_name, или сообщения об ошибке
    assert get_name(doc_number, documents) == expected_name


# Параметрический тест для функции get_directory
@pytest.mark.parametrize("doc_number,expected_directory", [
    ("2207 876234", '1'),
    ("11-2", '1'),
    ("10006", '2'),
    ("5455 028765", '1'),
    ("99999", "Полки с таким документом не найдено")
    # Тестовый случай отсутствия документа в директориях
])
def test_get_directory(init_data, doc_number, expected_directory):
    _, directories = init_data
    # Проверка на соответствие ожидаемому значению директории,
    # или сообщения об ошибке
    assert get_directory(doc_number, directories) == expected_directory


# Параметрический тест для функции add
@pytest.mark.parametrize("document_type,number,name,shelf_number", [
    ('international passport', '311 020203', 'Александр Пушкин', '3'),
    ('visa', '1234 567890', 'Иван Иванов', '1')
])
def test_add(init_data, document_type, number, name, shelf_number):
    documents, directories = init_data
    # Проверка на добавление нового документа в documents и directories
    new_documents, new_directories = add(
        document_type, number, name, shelf_number, documents, directories)
    # Проверяем его наличие в списках после добавления
    assert any(
        doc['number'] == number for doc in new_documents), "Документ не найден в documents"
    # Проверяем его наличие в директории после добавления
    assert shelf_number in new_directories and number in new_directories[
        shelf_number], "Документ не найден в directories"
