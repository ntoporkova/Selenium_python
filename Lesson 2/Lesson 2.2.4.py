#from selenium import webdriver

#browser = webdriver.Chrome()
#link = "https://SunInJuly.github.io/execute_script.html"
#browser.get(link)
#button = browser.find_element_by_tag_name("button")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#button.click()
#assert True


from selenium import webdriver
import math

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
#print(y)
browser.execute_script("window.scrollBy(0, 100);")
input1 = browser.find_element_by_css_selector("#answer")
input1.send_keys(str(y))
option1 = browser.find_element_by_css_selector("#robotCheckbox")
option1.click()
option2 = browser.find_element_by_css_selector("#robotsRule")
option2.click()
button = browser.find_element_by_css_selector("button.btn")
button.click()

