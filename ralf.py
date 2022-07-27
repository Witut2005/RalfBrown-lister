
import argparse
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

Parser = argparse.ArgumentParser()
Parser.add_argument('-ax', help='value of ah register', required=False)
Parser.add_argument('-ah', help='value of ah register', required=False)
Parser.add_argument('-int', help='interrupt number', required=True)

Args = Parser.parse_args()

print(Args.int)
print(Args.ah)
print(Args.ax)

try:
    int(Args.int, 16)
    int(Args.ah, 16)
    int(Args.ax, 16)

except TypeError:
    print('1')

DRIVER_PATH = str(os.environ["HOME"]) + "/chromedriver/chromedriver"

caps = DesiredCapabilities.CHROME
caps['pageLoadStrategy'] = 'eager'

driver = webdriver.Chrome(executable_path=DRIVER_PATH, desired_capabilities=caps)
driver.get('https://www.ctyme.com/intr/int.htm')
# driver.implicitly_wait(10)

interrupt_list = driver.find_elements(By.XPATH, '/html/body/center[2]/p[2]/table/tbody/tr/td/a')

# for ints in interrupt_list:
print(interrupt_list[Args.int].get_property('href'))
interrupt_list[Args.int].click()



# driver.quit()
