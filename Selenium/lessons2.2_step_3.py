from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    fname = browser.find_element_by_name("firstname").send_keys("Ivan")
    lname = browser.find_element_by_name("lastname").send_keys("Petrov")
    mail = browser.find_element_by_name("email").send_keys("1@mail.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file_step_3.txt')
    file = browser.find_element_by_id("file").send_keys(file_path)
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



