from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name("trollface.btn.btn-primary")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_id("input_value").text
    y = calc(int(x))
    result = browser.find_element_by_id("answer")
    result.send_keys(y)
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()