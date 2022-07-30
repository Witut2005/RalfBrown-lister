
import argparse
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

Parser = argparse.ArgumentParser()

Parser.add_argument('-param', help='parameters', required=True)

Args = Parser.parse_args()

int_number = int(Args.param[0] + Args.param[1], 16)
Args.param = 'Int ' + Args.param
print(Args.param)

DRIVER_PATH = str(os.environ["HOME"]) + "/chromedriver/chromedriver"

caps = DesiredCapabilities.CHROME
caps['pageLoadStrategy'] = 'eager'

driver = webdriver.Chrome(executable_path=DRIVER_PATH, desired_capabilities=caps)
driver.get('https://www.ctyme.com/intr/int.htm')
# driver.implicitly_wait(10)

interrupt_list = driver.find_elements(By.XPATH, '/html/body/center[2]/p[2]/table/tbody/tr/td/a')

interrupt_list[int_number].click()

results = (driver.find_elements(By.XPATH, '/html/body/p[4]/a'), driver.find_elements(By.XPATH, '/html/body/p[4]/a/b'))

print(results[1][0].text)

x = 0
while results[1][x].text != Args.param:
    x += 1

print(results[1][x].text)

results[0][x].click()

results = driver.find_elements(By.XPATH, '/html/body/pre')

for result in results:
    print(result.text)



# driver.quit()
