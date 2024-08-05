import requests
import unittest


class TestYandexDiskAPI(unittest.TestCase):
    base_url = 'https://cloud-api.yandex.net/v1/disk'
    headers = {
        'Authorization': 'OAuth  '
        # Вставьте ваш токен здесь
    }

    def test_create_folder_success(self):
        folder_name = 'TestFolder'
        folder_info_url = f'{self.base_url}/resources?path=/{folder_name}'

        # Проверьте, существует ли уже папка с данным именем
        response = requests.get(folder_info_url, headers=self.headers)
        if response.status_code == 200:
            # Папка уже существует, просто проверьте успешный ответ
            self.assertEqual(response.status_code, 200)
        else:
            # Папка не существует, создайте ее
            folder_url = f'{self.base_url}/resources?path=/{folder_name}'
            response = requests.put(folder_url, headers=self.headers)
            self.assertEqual(response.status_code, 201)  # Папка успешно создана

        # Убедитесь, что папка действительно создана и отображается в списке файлов.
        response = requests.get(folder_info_url, headers=self.headers)
        self.assertEqual(response.status_code, 201)  # Запрос информации о папке успешен

    def test_create_folder_error(self):
        folder_name = 'TestFolder'
        folder_url = f'{self.base_url}/resources?path=/{folder_name}'

        # Попытайтесь создать папку с тем же именем, что и у существующей папки.
        response = requests.put(folder_url, headers=self.headers)
        self.assertEqual(response.status_code, 409)  # Конфликт, папка уже существует

    def test_invalid_authorization(self):
        invalid_headers = {
            'Authorization': 'InvalidToken',  # Неверный токен
        }
        folder_name = 'InvalidTestFolder'
        folder_url = f'{self.base_url}/resources?path=/{folder_name}'

        # Попытка создать папку с недействительным токеном авторизации.
        response = requests.put(folder_url, headers=invalid_headers)
        self.assertEqual(response.status_code, 409)  # Несанкционированный

    def test_upload_file_success(self):
        folder_name = 'TestFolder'
        file_name = 'tasks/test_file.txt'
        file_url = f'{self.base_url}/resources/upload?path=/{folder_name}/{file_name}'

        # Загрузите файл в созданную папку.
        with open(file_name, 'rb') as file:
            response = requests.put(file_url, headers=self.headers, data=file)
            self.assertEqual(response.status_code, 201)  # Файл успешно загружен
            # Убедитесь, что файл действительно загружен и отображается в списке файлов.
            file_info_url = f'{self.base_url}/resources?path=/{folder_name}/{file_name}'
        # Создать тестовый файл для загрузки (можно удалить после тестирования)
        with open(file_name, 'w') as file:
            file.write('This is a test file.')
            response = requests.get(file_info_url, headers=self.headers)
            self.assertEqual(response.status_code, 201)  # Файл успешно загружен
            # Удалить тестовый файл после тестирования
            file.close()

    # Удалить тестовую папку после тестирования
    def test_delete_folder_success(self):
        folder_name = 'TestFolder'
        folder_url = f'{self.base_url}/resources?path=/{folder_name}'

        # Удалите созданную папку.
        response = requests.delete(folder_url, headers=self.headers)
        self.assertEqual(response.status_code, 204)  # Папка успешно удалена


if __name__ == '__main__':
    unittest.main()
