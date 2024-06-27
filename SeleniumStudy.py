import time
from test import test_print
from selenium import webdriver
from selenium.webdriver.common.by import By

test_print()
driver = webdriver.ChromiumEdge()

driver.maximize_window()
driver.get("https://www.bilibili.com")

kw = driver.find_element(By.CLASS_NAME,"nav-search-input")
kw.send_keys("cs")
submit = driver.find_element("class name","nav-search-btn")
submit.click()

driver.back()
driver.forward()

driver.refresh()
time.sleep(5)

print("%r" % "quit")
driver.quit()
