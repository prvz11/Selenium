from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(x))))


link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value").text
    y = calc(int(x))
    y_element = browser.find_element_by_id("answer")
    y_element.send_keys(y)
    button = browser.find_element_by_class_name("btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    x_element = browser.find_element_by_id("robotCheckbox")
    x_element.click()
    x_element = browser.find_element_by_id("robotsRule")
    x_element.click()
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
