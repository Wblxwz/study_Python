import time

from selenium import webdriver

options = webdriver.ChromeOptions()

driver = webdriver.Remote(command_executor="http://192.168.41.1:4444/wd/hub",options=options)
driver.get("https://www.baidu.com")
js = "alert(123)"
driver.execute_script(js)
driver.switch_to.alert.accept()

time.sleep(2)
driver.quit()