from selenium import webdriver
from selenium.webdriver.support.ui import Select


def calc(input1, input2):
    return str(int(input1)+int(input2))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects2.html')
x = browser.find_element_by_id('num1')
y = browser.find_element_by_id('num2')
output = calc(x.text, y.text)
#print(output)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(output)

button = browser.find_element_by_css_selector("button.btn")
button.click()

