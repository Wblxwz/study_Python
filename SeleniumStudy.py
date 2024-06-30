import csv
import time
import logging
from test import test_print
#webdriver
from selenium import webdriver
#getElement所需
from selenium.webdriver.common.by import By
#鼠标操作
from selenium.webdriver.common.action_chains import ActionChains
#键盘操作
from selenium.webdriver.common.keys import Keys
#等待元素，适用于异步加载
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#通过模块化、参数化的方式进行自动化测试，减少冗余代码
test_print()
#打印日志，selenium是B/S架构，通过http请求控制浏览器自动化测试
#logging.basicConfig(level=logging.DEBUG)
driver = webdriver.ChromiumEdge()

driver.maximize_window()
driver.get("https://www.bilibili.com")
#driver.refresh()

fj = driver.find_element(By.CLASS_NAME,"channel-link")
ActionChains(driver).context_click(fj).perform()
print(fj.text)
print(driver.title,driver.current_url)
print(fj.get_attribute("href"))

zy = driver.find_element(By.LINK_TEXT,"综艺")
ActionChains(driver).click(zy).perform()
print(driver.get_cookies())
ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[1]/ul[1]/li[4]/a")).perform()
js = "alert(123)"
driver.execute_script(js)
driver.switch_to.alert.accept()
kw = driver.find_element(By.CLASS_NAME,"nav-search-input")
kw.send_keys(Keys.F5)
kw.send_keys("cs")
submit = driver.find_element("class name","nav-search-btn")
submit.click()

driver.back()
driver.forward()

#等待异步加载时的对象
try:
    element = WebDriverWait(driver,1,0.5).until(EC.presence_of_element_located((By.CLASS_NAME,"nav-search-input1")))
    print(element.get_attribute("title"))
except Exception:
    print("no")
try:
    EC.title_is("aaa")
except Exception:
    print("e")
finally:
    print(1)

time.sleep(3)

print("%r" % "quit")
driver.quit()

with open("./test.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)