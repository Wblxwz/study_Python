import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def waitIframe(driver,id):
    try:
        driver.find_element(By.ID,id)
    except Exception as e:
        return False
    return True

def logIn(webDriver):

    if webDriver == "Edge":
        driver = webdriver.Edge()

        driver.get("https://www.douyu.com")
        driver.maximize_window()

        actionChains = ActionChains(driver)
        hover = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"/html/body/header/div/div/div[1]/div[3]/div[7]/div/div")))
        actionChains.move_to_element(hover).perform()
        logIn = driver.find_element(By.XPATH,"/html/body/header/div/div/div[1]/div[3]/div[7]/div/div/div/div/div/div[2]/a[1]")
        logIn.click()

        WebDriverWait(driver,5).until(lambda driver:waitIframe(driver,"login-passport-frame"))
        driver.switch_to.frame("login-passport-frame")
        logInByPwd = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[2]/div[1]/div[2]")))
        ActionChains(driver).click(logInByPwd).perform()

        niCheng = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div[2]/div/div[1]/span[2]")
        niCheng.click()

        nc = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div[2]/div/form/div[2]/div/input")
        nc.send_keys("111111")
        pwd = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div[2]/div/form/div[3]/input[1]")
        pwd.send_keys("111111")

        logInBtn = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div[2]/div/form/div[6]/input")
        ActionChains(driver).click(logInBtn).perform()

        time.sleep(300)
        myFollow = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,"/html/body/header/div/div/div[1]/div[3]/div[3]")))
        ActionChains(driver).move_to_element(myFollow).perform()

        time.sleep(300)

        driver.quit()

if __name__ == "__main__":
    logIn("Edge")