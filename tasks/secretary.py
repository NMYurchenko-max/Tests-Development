documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {
        "type": "driver license",
        "number": "5455 028765",
        "name": "Василий Иванов"},
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_name(doc_number, documents):
    for doc in documents:
        if doc_number == doc['number']:
            return doc['name']
    return 'Документ не найден'


def get_directory(doc_number, directories):
    for direct in directories:
        if doc_number in directories[direct]:
            return direct
    return 'Полки с таким документом не найдено'


def add(document_type, number, name, shelf_number, documents, directories):
    for direct in directories:
        if shelf_number == direct:
            directories[direct].append(number)
            documents.append({
                "type": document_type,
                "number": number,
                "name": name
            })
            return documents, directories

    directories[shelf_number] = [number]
    documents.append({"type": document_type, "number": number, "name": name})

    return documents, directories


if __name__ == '__main__':
    print(get_name("10006", documents))
    print(get_directory("11-2", directories))
    print(get_name("101", documents))
    documents, directories = add(
        'international passport',
        '311 020203',
        'Александр Пушкин', '3', documents, directories)
    print(get_directory("311 020203", directories))
    print(get_name("311 020203", documents))
    print(get_directory("311 020204", directories))
