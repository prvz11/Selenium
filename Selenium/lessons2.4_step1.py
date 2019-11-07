from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price1 = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_id("book").click()
    x = browser.find_element_by_id("input_value").text
    y = calc(int(x))
    resuly = browser.find_element_by_id("answer").send_keys(y)
    button = browser.find_element_by_id("solve").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()