from selenium import webdriver
import math
link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
#test
x_element = browser.find_element_by_id("treasure")
x=x_element.get_attribute("valuex")
#print(chest)
y = calc(x)
#print(y)
input1 = browser.find_element_by_css_selector("#answer")
input1.send_keys(str(y))
option1 = browser.find_element_by_css_selector("#robotCheckbox")
option1.click()
option2 = browser.find_element_by_css_selector("#robotsRule")
option2.click()
button = browser.find_element_by_css_selector("button.btn")
button.click()