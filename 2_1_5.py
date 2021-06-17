from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/math.html"
    browser.get(link)

    val = browser.find_element_by_id("input_value").text
    field = browser.find_element_by_id("answer")
    field.send_keys(calc(val))
    check = browser.find_element_by_id("robotCheckbox")
    check.click()

    rad = browser.find_element_by_css_selector('[value="robots"]')
    rad.click()

    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()    
