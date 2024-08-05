import unittest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestYandexAuth(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_yandex_auth(self):
        driver = self.driver
        driver.get("https://passport.yandex.ru/auth/")

        username_field = driver.find_element(By.ID, "passp-field-login")
        username_field.clear()  # Очистка поля перед вводом нового значения
        username_field.send_keys("your_username")  # Замените "your_username" на ваш логин

        password_field = driver.find_element(By.ID, "passp-field-passwd")
        password_field.clear()  # Очистка поля перед вводом нового значения
        password_field.send_keys("your_password")  # Замените "your_password" на ваш пароль

        password_field.send_keys(Keys.RETURN)

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Личные данные')]"))
            )
            print("Авторизация прошла успешно.")
        except TimeoutException:
            print("Авторизация не удалась.")


if __name__ == "__main__":
    unittest.main()
    # Запуск теста: python -m unittest tests/test_autorizationg.py