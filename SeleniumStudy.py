import time
from test import test_print
from selenium import webdriver

test_print()
driver = webdriver.ChromiumEdge()

driver.get("https://www.baidu.com")

kw = driver.find_element("id","kw")
kw.send_keys("cs")
submit = driver.find_element("id","su")
submit.click()

time.sleep(5)

print("%r" % "quit")
driver.quit()
