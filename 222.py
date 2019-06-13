from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_xpath_form")
elements = browser.find_elements_by_xpath('//button[text()="Отправить"]')
for element in elements:
    element.send_keys("Мой ответ")

button = browser.find_element_by_css_selector("button.btn")
button.click()
