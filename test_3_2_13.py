import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        labels = browser.find_elements(By.TAG_NAME, 'label')  # Список label
        inputs = browser.find_elements(By.TAG_NAME, 'input')  # Список input

        for i, label in enumerate(labels):
            if label.text[-1] == '*':
                inputs[i].send_keys('test')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual( welcome_text, "Congratulations! You have successfully registered!", "Yes")

        time.sleep(10)
        browser.quit()

    # Тест выполняемый с ошибкой из-за отсутствующего поля
    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CLASS_NAME, 'first_block .first')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CLASS_NAME, 'first_block .second')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, 'first_block .third')
        input3.send_keys("email@test.ru")
        input4 = browser.find_element(By.CLASS_NAME, 'second_block .first')
        input4.send_keys("+798765456")
        input5 = browser.find_element(By.CLASS_NAME, "second_block .second")
        input5.send_keys("Russia")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Yes")

        time.sleep(10)
        browser.quit()


if __name__ == "__main__":
    unittest.main()