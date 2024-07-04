from selenium import webdriver

options = webdriver.ChromeOptions()

driver = webdriver.Remote(command_executor="http://192.168.41.1:4444/wd/hub",options=options)
driver.get("https://www.baidu.com")
driver.refresh()

driver.quit()