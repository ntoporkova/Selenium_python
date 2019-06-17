from selenium import webdriver
import math

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector('button.btn')
button.click()


#new_window = browser.window_handles['CDwindow-E2A6DC20B42F129B311E70AE364A6AAA')]
#print(len(browser.window_handles))
new_window1 = browser.window_handles[len(browser.window_handles)-1]
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
#print(new_window)



def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
print(y)
input = browser.find_element_by_id('answer')
input.send_keys(str(y))
button = browser.find_element_by_css_selector('button.btn')
button.click()
